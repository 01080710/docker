def get_config(mode='low'):
    configs = {
        'low':    (1,  (0, 0), 100, '安全穩定模式'),
        'middle': (5,  (0, 0), 100, '效能優化模式'),
        'high':   (20, (0, 0), 100, '極限處理模式'),
    }
    # 使用 .get() 避免輸入錯誤的 mode 時程式崩潰
    return configs.get(mode, configs['low'])

