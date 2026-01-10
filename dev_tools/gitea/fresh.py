from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import random ,math ,asyncio,aiohttp,json
import undetected_chromedriver as uc
from datetime import datetime
from bs4 import BeautifulSoup
from tqdm.asyncio import tqdm
from config import get_config
import pandas as pd



### 使用方式
sem_limit, sleep_range, per_page, desc = get_config('high')

### 共用設定
def selenium_login():
    driver = uc.Chrome(
        driver_executable_path=r'C:\Users\88696\Desktop\tixcraft_bot\webdriver\chromedriver.exe'
    )
    try:
        url ="https://tickets.vantagemarkets.com/support/login"
        driver.get(url)

        #等 username 輸入框出現
        WebDriverWait(driver,20).until(
            EC.presence_of_element_located((By.ID, "username"))
        )

        driver.find_element (By.ID,"username").send_keys("Deposit@vantagemarkets.com")
        driver.find_element(By.ID, "password").send_keys("Vantagenumber1")

        login_btn = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[2]/div/div/div/div/div/div[2]/div[1]/form/div[1]/div[4]/div/button'))
        )
        login_btn.click()
        old_url = driver.current_url

        # 等 URL 改嫈（登入成功或重導向）
        WebDriverWait(driver, 120).until(
            lambda d:d.current_url != old_url
        )
        #等 session cookie 出現
        WebDriverWait(driver, 120).until(
            lambda d: any(c['name'] == 'helpdesk_node_session' for c in d.get_cookies())
        )

        #取 cookies + user-agent
        cookies = {c['name']: c['value'] for c in driver.get_cookies()}
        user_agent = driver.execute_script("return navigator.userAgent;")
        return cookies, user_agent
    except Exception as e:
        print(e)
    finally:
        driver.quit()

BASE_URL = 'https://tickets.vantagemarkets.com/api/_'
PER_PAGE = per_page
SEM_LIMIT = sem_limit # 同時請求數（可調 5~20）

headers = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
    'referer': 'https://tickets.vantagemarkets.com/a/tickets/view/new_and_my_open',
    }


# html transformer
def extract_plain_text(text):
    if pd.isna(text):
        return text
    soup = BeautifulSoup(text,"html.parser")
    return soup.get_text(separator=" ").strip()


# generate_json
async def fetch_json(session, url, params=None, retries=3):
    for i in range(retries):
        try:
            async with session.get(url, params=params) as resp:
                if resp.status == 429: # Too Many Requests
                    retry_after = int(resp.headers.get ("Retry-After", "2"))
                    print(f"429，等待 {retry_after}s 後重試..")
                    await asyncio.sleep(retry_after)
                    continue
                resp.raise_for_status()
                return await resp.json()
        except aiohttp.ClientResponseError as e:
            if i < retries - 1:
                print(f"請求失敗，重試{i+1}/{retries}...")
                await asyncio.sleep(2)
            else:
                raise 


folder_metadata = {
        'D1': {
            'group_id': "21000393306",
            'tag': "D1. Deposit Failure",
            'filename': "DepositFailure_Report"
        },
        'D6': {
            'group_id': "21000567209",
            'tag': "D6. Missing Deposit to HA",
            'filename': "MissingDeposit_Report"
        }
    }

# 定義每個 Folder 的差異化參
def generate_query_hash(folder_key):
    
    meta = folder_metadata.get(folder_key)
    if not meta:
        raise ValueError(f"找不到 {folder_key} 的配置資訊")

    # 定義結構化的原始資料（Python List/Dict）
    query_structure = [
        {"value": [{"id": 1}], "condition": "workspace_id", "operator": "is_in", "type": "default"},
        {"value": [meta['group_id']], "condition": "group_id", "operator": "is_in", "type": "default"},
        {"value": "six_months", "condition": "created_at", "operator": "is_greater_than", "type": "default"},
        {"value": [meta['tag']], "condition": "tags", "operator": "is_in", "type": "default"}
    ]
    
    # 轉換成 API 需要的字串格式
    return json.dumps(query_structure)


# Categories 
async def process_ticket_D1(session ,ticket, sem, sleep_range) :
    async with sem:
        delay = random.uniform(*sleep_range) # 使用 * 展開 tuple
        await asyncio.sleep(delay)
        ticket_id = ticket['id']
        subject = ticket['subject']
        human_display_id = ticket['human_display_id']
        requester = ticket['requester']
        job_title = requester.get('job_title',None)
        name = requester.get('name',None)
        email = requester.get('email',None)
        phone = requester.get('phone',None)
        
        # - requested_items -
        items = await fetch_json(
            session, 
            f'{BASE_URL}/tickets/{ticket_id}/requested_items'
        )

        item_id = items['requested_items'][0]['id']
        
        
        # requested_item detail------...
        detail = await fetch_json(
            session,
            f'{BASE_URL}/tickets/{ticket_id}/requested_items/{item_id}', 
            params= {'view': 'more_info'}
        )
        
        ri = detail['requested_item']
        image = ri['attachments'][0]['attachment_url'] if ri.get('attachments') else None
        created_at = ri['attachments'][0]['created_at'] if ri.get('attachments') else None
        updated_at = ri['attachments'][0]['updated_at'] if ri.get('attachments') else None
        
        description = extract_plain_text(ri['item']['short_description'])
        cf = ri.get ('custom_fields', {})

        action_type = cf.get('what_would_you_like_to_know_do',None)
        regulation = cf.get('regulation',None)
        user_id = cf.get('client_s_registered_mail',None)
        account_no = cf.get('account_number',None)
        deposit_way = cf.get('way_of_deposit',None)
        user_note = cf.get('note',None)
        zendesk_id = cf.get('zendesk_id_for_cs_team_only',None)


        return {
            "created_at": created_at,
            "updated_at": updated_at,
            "subject": subject,
            "ticket_id": human_display_id,  # 建議縮短
            # "job_title": job_title,
            "user_name": name,
            "user_email": email,
            # "user_phone": phone,
            "attachment_url": image,        # 建議標註為 URL
            "description": description,
            "action_type": action_type,
            "regulation": regulation,
            "client_email": user_id,        # 既然是 mail，命名為 client_email 更準確
            "account_no": account_no,
            "deposit_method": deposit_way,  # 使用 method 更專業 
            "remark": user_note,            # 簡化為備註
            "zendesk_id": zendesk_id,
        }


async def process_ticket_D6(session ,ticket, sem, sleep_range) :
    async with sem:
        delay = random.uniform(*sleep_range) # 使用 * 展開 tuple
        await asyncio.sleep(delay)
        ticket_id = ticket['id']
        subject = ticket['subject']
        human_display_id = ticket['human_display_id']
        requester = ticket['requester']
        job_title = requester.get('job_title',None)
        name = requester.get('name',None)
        email = requester.get('email',None)
        phone = requester.get('phone',None)
        
        # - requested_items -
        items = await fetch_json(
            session, 
            f'{BASE_URL}/tickets/{ticket_id}/requested_items'
        )

        item_id = items['requested_items'][0]['id']
        
        # conversations
        conv = await fetch_json(
            session, 
            f'{BASE_URL}/tickets/{ticket_id}/conversations', 
            params={'include': 'user, phone, feedback', 'per_page': 3}
        )

        df = pd.json_normalize(conv['conversations'])
        first_text = None
        if 'body_text' in df:
            mask = df['body_text']. str.contains('#', na=False)
            if mask.any():
                first_text = df.loc[mask, 'body_text'].iloc[0]
        
        # requested_item detail------...
        detail = await fetch_json(
            session,
            f'{BASE_URL}/tickets/{ticket_id}/requested_items/{item_id}', 
            params= {'view': 'more_info'}
        )
        
        ri = detail['requested_item']
        image = ri['attachments'][0]['attachment_url'] if ri.get('attachments') else None
        created_at = ri['attachments'][0]['created_at'] if ri.get('attachments') else None
        updated_at = ri['attachments'][0]['updated_at'] if ri.get('attachments') else None
        description = extract_plain_text(ri['item']['description'])
        cf = ri.get ('custom_fields', {})
        Merchant_number = cf.get('merchant_number',None)
        Merchant_Order = cf.get('merchant_order',None)
        Account_Number = cf.get('account_number',None)
        Receipt_Currency = cf.get('currency',None)
        Issue_encountered = cf.get('issue_encountered',None)
        More_information = cf.get('more_information',None)

        return {
            "created_at": created_at,
            "updated_at": updated_at,
            "subject": subject,
            "ticket_id": human_display_id,
            "job_title": job_title,
            "user_name": name,
            "user_email": email,
            "user_phone": phone,
            "attachment_url": image,
            "bot_feedback": first_text,
            "description": description,
            "merchant_no": Merchant_number,
            "merchant_order": Merchant_Order,
            "account_no": Account_Number,
            "currency": Receipt_Currency,
            "issue_type": Issue_encountered,
            "more_info": More_information
        }


async def main(cookies, user_agent, folder, handler):
    
    headers= {
        'user-agent': user_agent,
        'accept':'*/*',
        'referer': 'https://tickets.vantagemarkets.com/a/tickets/view/new_and_my_open',
    }

    sem = asyncio.Semaphore(SEM_LIMIT)
    async with aiohttp.ClientSession(headers=headers, cookies=cookies) as session:

        # 撰寫動態資料夾欄位
        # folder = 'D6'
        params = {
            'filter': 'all_tickets',
            'include': 'stats, responder, requester, ticket_states, ticket_status, group',
            'order_by': 'created_at',
            'order_type': 'desc',
            'page': 1,
            'per_page': PER_PAGE,
            'query_hash': generate_query_hash(folder),
            'workspace_id': '1',
        }

        first = await fetch_json(session, f'{BASE_URL}/tickets', params)
        total = first['meta']['count']
        pages = math.ceil(total / PER_PAGE)

        datalists = []
        for page in range(10):
            print(f'目前執行到第{page+1}頁')
            params ['page'] = page + 1
            data = await fetch_json(session, 
                                    f'{BASE_URL}/tickets', 
                                    params)
            tasks = [
                handler(session, ticket, sem, sleep_range)
                for ticket in data['tickets']
            ]
            
            results = await tqdm.gather(
                *tasks,
                desc=f'第{page+1}頁處理中',
                total=len(tasks)
            )
            datalists.extend(results)

        df = pd.DataFrame(datalists)
        
        # Working storageEXCEL
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"{folder_metadata[folder]['filename']}({timestamp}).xlsx"
        df.to_excel(filename, index=False,engine='openpyxl')
        return df


if __name__ == "__main__":
    cookies, ua = selenium_login()
    folder = 'D6'
    df = asyncio.run(main(cookies, ua, folder, process_ticket_D6))
    # print(df.head(10))