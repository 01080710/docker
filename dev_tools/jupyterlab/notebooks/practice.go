{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "3d8b0b7b-473e-4251-86ec-2ebc36f467b6",
   "metadata": {},
   "source": [
    "✅ 1. 常數 const + iota"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "319cb11f-46bc-4f63-abc0-7415718c3c7f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Pi = 3.14\n",
      "A: 0 B: 1 C: 2\n"
     ]
    }
   ],
   "source": [
    "package main\n",
    "import \"fmt\"\n",
    "\n",
    "const Pi = 3.14\n",
    "\n",
    "// iota：自動遞增常數\n",
    "const (\n",
    "    A = iota // 0\n",
    "    B        // 1\n",
    "    C        // 2\n",
    ")\n",
    "\n",
    "func main() {\n",
    "    fmt.Println(\"Pi =\", Pi)\n",
    "    fmt.Println(\"A:\", A, \"B:\", B, \"C:\", C)\n",
    "}\n",
    "\n",
    "main()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "af4efeeb-e39b-4db3-87dd-ed6867304d5d",
   "metadata": {},
   "source": [
    "✅ 2. 條件判斷：if / else"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "bfce2c04-c2d8-4bbf-bab2-45dcc9224306",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "成年人\n"
     ]
    }
   ],
   "source": [
    "package main\n",
    "import \"fmt\"\n",
    "\n",
    "func main() {\n",
    "    age := 20\n",
    "\n",
    "    if age >= 18 {\n",
    "        fmt.Println(\"成年人\")\n",
    "    } else {\n",
    "        fmt.Println(\"未成年\")\n",
    "    }\n",
    "}\n",
    "\n",
    "main()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "157047a3-e031-4cf8-8087-d3aa41aed367",
   "metadata": {},
   "source": [
    "✅ 3. switch"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "c4937054-e74e-4876-84af-3eb5ecd2b3ba",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "星期三\n"
     ]
    }
   ],
   "source": [
    "package main\n",
    "import \"fmt\"\n",
    "\n",
    "func main() {\n",
    "    day := 3\n",
    "    switch day {\n",
    "    case 1:\n",
    "        fmt.Println(\"星期一\")\n",
    "    case 2:\n",
    "        fmt.Println(\"星期二\")\n",
    "    case 3:\n",
    "        fmt.Println(\"星期三\")\n",
    "    case 4:\n",
    "        fmt.Println(\"星期四\")\n",
    "    case 5:\n",
    "        fmt.Println(\"星期五\")\n",
    "    case 6:\n",
    "        fmt.Println(\"星期六\")\n",
    "    case 7:\n",
    "        fmt.Println(\"星期日\")\n",
    "    default:\n",
    "        fmt.Println(\"其他天\")\n",
    "    }\n",
    "}\n",
    "\n",
    "main()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "216a7dcb-bc57-4e2c-bf38-c00aa80f0e5c",
   "metadata": {},
   "source": [
    "✅ 4. Array vs Slice"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "3bcdd777-9802-44cf-aecd-e359a75381c1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Array: [1 2 3]\n",
      "Slice: [4 5 6]\n"
     ]
    }
   ],
   "source": [
    "package main\n",
    "import \"fmt\"\n",
    "\n",
    "func main() {\n",
    "    var arr = [3]int{1, 2, 3}        // 陣列：固定長度\n",
    "    slice := []int{4, 5, 6}          // Slice：可變長度\n",
    "\n",
    "    fmt.Println(\"Array:\", arr)\n",
    "    fmt.Println(\"Slice:\", slice)\n",
    "}\n",
    "\n",
    "main()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a6299ab1-edde-4ad0-9825-d92833f34c2e",
   "metadata": {},
   "source": [
    "✅ 5. Struct（結構）"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "058e6c1e-7d67-400d-8dcd-687529b37fb5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Person 1 Name: Alice\n",
      "Person 2 Age: 25\n",
      "Updated Person 1: {Alice 31 New York}\n",
      "Person 3: { 0 }\n"
     ]
    }
   ],
   "source": [
    "package main\n",
    "import \"fmt\"\n",
    "\n",
    "// 定義一個名為 Person 的結構體\n",
    "type Person struct {\n",
    "    Name   string\n",
    "    Age    int\n",
    "    City   string\n",
    "}\n",
    "\n",
    "func main() {\n",
    "    // 創建 Person 結構體的實例\n",
    "    person1 := Person{Name: \"Alice\", Age: 30, City: \"New York\"}\n",
    "    person2 := Person{\"Bob\", 25, \"London\"} // 可以省略字段名，但需按定義順序賦值\n",
    "\n",
    "    // 訪問結構體的字段 (使用點 .)\n",
    "    fmt.Println(\"Person 1 Name:\", person1.Name)\n",
    "    fmt.Println(\"Person 2 Age:\", person2.Age)\n",
    "\n",
    "    // 修改結構體的字段\n",
    "    person1.Age = 31\n",
    "    fmt.Println(\"Updated Person 1:\", person1)\n",
    "\n",
    "    // 創建一個未初始化的結構體，字段會被賦予零值\n",
    "    var person3 Person\n",
    "    fmt.Println(\"Person 3:\", person3) // 輸出: Person 3: { 0 }\n",
    "}\n",
    "main()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d0be7e80-d995-4d4e-ae84-b37f03bf7bc8",
   "metadata": {},
   "source": [
    "✅ 6. Pointer（指標）"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "5695781d-4a37-42fb-9afd-6d17e47199e0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "x = 11\n"
     ]
    }
   ],
   "source": [
    "package main\n",
    "import \"fmt\"\n",
    "\n",
    "func addOne(n *int) {\n",
    "    *n += 1\n",
    "}\n",
    "\n",
    "func main() {\n",
    "    x := 10\n",
    "    addOne(&x)\n",
    "    fmt.Println(\"x =\", x) // 輸出 11\n",
    "}\n",
    "\n",
    "main()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b908bc86-150e-42b1-8d2d-27b158c0affc",
   "metadata": {},
   "source": [
    "✅ 7. defer：延遲執行"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "9716acf4-104b-4f13-a8f6-cfa014a1ae34",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "先印這個\n",
      "最後印出\n"
     ]
    }
   ],
   "source": [
    "package main\n",
    "import \"fmt\"\n",
    "\n",
    "func main() {\n",
    "    defer fmt.Println(\"最後印出\")\n",
    "    fmt.Println(\"先印這個\")\n",
    "}\n",
    "\n",
    "main()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f202e163-cc5a-41ea-8a2d-f6b00d8fc36f",
   "metadata": {},
   "source": [
    "✅ 8. panic / recover（錯誤處理）"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "ea53c3f8-8c04-49ba-a3fd-72709d446072",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "發現錯誤: 出事啦！\n",
      "繼續執行\n"
     ]
    }
   ],
   "source": [
    "package main\n",
    "import \"fmt\"\n",
    "\n",
    "func risky() {\n",
    "    defer func() {\n",
    "        if r := recover(); r != nil {\n",
    "            fmt.Println(\"發現錯誤:\", r)\n",
    "        }\n",
    "    }()\n",
    "    panic(\"出事啦！\")\n",
    "}\n",
    "\n",
    "func main() {\n",
    "    risky()\n",
    "    fmt.Println(\"繼續執行\")\n",
    "}\n",
    "\n",
    "main()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3afb29c5-a739-42e8-aa6c-1b93abc12243",
   "metadata": {},
   "source": [
    "✅ 9. error 型別處理"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "2e432e3b-47af-4d70-98de-5673e45b351f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "錯誤: 除數不能為 0\n"
     ]
    }
   ],
   "source": [
    "package main\n",
    "import (\n",
    "    \"errors\"\n",
    "    \"fmt\"\n",
    ")\n",
    "\n",
    "func divide(a, b float64) (float64, error) {\n",
    "    if b == 0 {\n",
    "        return 0, errors.New(\"除數不能為 0\")\n",
    "    }\n",
    "    return a / b, nil\n",
    "}\n",
    "\n",
    "func main() {\n",
    "    result, err := divide(10, 0)\n",
    "    if err != nil {\n",
    "        fmt.Println(\"錯誤:\", err)\n",
    "    } else {\n",
    "        fmt.Println(\"結果:\", result)\n",
    "    }\n",
    "}\n",
    "\n",
    "main()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1982fa8d-fe53-46bc-889e-61593c10e446",
   "metadata": {},
   "source": [
    "✅ 10. 匿名函式與閉包（closure）"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "a7dd93c7-b490-494c-a987-807b8bb9bc51",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "counter = 2\n"
     ]
    }
   ],
   "source": [
    "package main\n",
    "import \"fmt\"\n",
    "\n",
    "func main() {\n",
    "    counter := 0\n",
    "    increment := func() {\n",
    "        counter++\n",
    "    }\n",
    "\n",
    "    increment()\n",
    "    increment()\n",
    "    fmt.Println(\"counter =\", counter)\n",
    "}\n",
    "\n",
    "main()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "772d64a4-7e6d-47b8-9d6b-86545b7b27d1",
   "metadata": {},
   "source": [
    "✅ 11. 可變參數（Variadic Function）"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "613112b0-d526-482d-9aae-7f3c00649f11",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "總和: 10\n"
     ]
    }
   ],
   "source": [
    "package main\n",
    "import \"fmt\"\n",
    "\n",
    "func sum(nums ...int) int {\n",
    "    total := 0\n",
    "    for _, n := range nums {\n",
    "        total += n\n",
    "    }\n",
    "    return total\n",
    "}\n",
    "\n",
    "func main() {\n",
    "    fmt.Println(\"總和:\", sum(1, 2, 3, 4))\n",
    "}\n",
    "\n",
    "main()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c51600ab-1ab1-439b-bc7c-a47919a18008",
   "metadata": {},
   "source": [
    "✅ 12. goroutine（並行）"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "dff74dbf-5a9e-4f4a-9170-fd6fd3f736e0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "World\n",
      "Hello\n",
      "World\n",
      "Hello\n",
      "Hello\n",
      "World\n"
     ]
    }
   ],
   "source": [
    "package main\n",
    "import (\n",
    "    \"fmt\"\n",
    "    \"time\"\n",
    ")\n",
    "\n",
    "func say(msg string) {\n",
    "    for i := 0; i < 3; i++ {\n",
    "        fmt.Println(msg)\n",
    "        time.Sleep(500 * time.Millisecond)\n",
    "    }\n",
    "}\n",
    "\n",
    "func main() {\n",
    "    go say(\"Hello\")\n",
    "    say(\"World\")\n",
    "}\n",
    "\n",
    "main()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "38e615de-96e4-4b66-ab1f-fc37614143f0",
   "metadata": {},
   "source": [
    "✅ 13. channel（通道）"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "94caf625-c3c5-4e3c-9d5c-fa3e33f6a42c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "生產者：生產了 蘋果\n",
      "消費者：收到了 蘋果\n",
      "生產者：生產了 香蕉\n",
      "消費者：收到了 香蕉\n",
      "生產者：生產了 橘子\n",
      "消費者：收到了 橘子\n",
      "消費者：處理完所有資料\n"
     ]
    }
   ],
   "source": [
    "package main\n",
    "import (\n",
    "\t\"fmt\"\n",
    "\t\"time\"\n",
    ")\n",
    "\n",
    "// 資料生產者 goroutine\n",
    "func producer(ch chan string) {\n",
    "\tdata := []string{\"蘋果\", \"香蕉\", \"橘子\"}\n",
    "\tfor _, item := range data {\n",
    "\t\tfmt.Println(\"生產者：生產了\", item)\n",
    "\t\tch <- item // 將資料發送到 channel\n",
    "\t\ttime.Sleep(time.Second) // 模擬生產資料的時間\n",
    "\t}\n",
    "\tclose(ch) // 生產完畢後關閉 channel\n",
    "}\n",
    "\n",
    "// 資料消費者 goroutine\n",
    "func consumer(ch chan string) {\n",
    "\tfor msg := range ch { // 從 channel 接收資料，直到 channel 被關閉\n",
    "\t\tfmt.Println(\"消費者：收到了\", msg)\n",
    "\t\ttime.Sleep(500 * time.Millisecond) // 模擬處理資料的時間\n",
    "\t}\n",
    "\tfmt.Println(\"消費者：處理完所有資料\")\n",
    "}\n",
    "\n",
    "func main() {\n",
    "\tdataChannel := make(chan string) // 創建一個傳輸字串的 channel\n",
    "\n",
    "\tgo producer(dataChannel) // 啟動生產者 goroutine\n",
    "\tgo consumer(dataChannel) // 啟動消費者 goroutine\n",
    "\n",
    "\ttime.Sleep(5 * time.Second) // 等待一段時間讓 goroutine 完成工作\n",
    "}\n",
    "main()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c14ff459-136a-44c0-856c-909cf02f8b63",
   "metadata": {},
   "source": [
    "✅ 14. File I/O（寫入與讀取）"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "268930bf-3a6b-4da6-804c-1904c96dae6a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "檔案內容: Hello, File!\n"
     ]
    }
   ],
   "source": [
    "package main\n",
    "import (\n",
    "    \"fmt\"\n",
    "    \"io/ioutil\"\n",
    "    \"os\"\n",
    ")\n",
    "\n",
    "func main() {\n",
    "    // 寫入檔案\n",
    "    err := ioutil.WriteFile(\"sample.txt\", []byte(\"Hello, File!\"), 0644)\n",
    "    if err != nil {\n",
    "        fmt.Println(\"寫入錯誤:\", err)\n",
    "    }\n",
    "\n",
    "    // 讀取檔案\n",
    "    data, err := ioutil.ReadFile(\"sample.txt\")\n",
    "    if err != nil {\n",
    "        fmt.Println(\"讀取錯誤:\", err)\n",
    "    }\n",
    "\n",
    "    fmt.Println(\"檔案內容:\", string(data))\n",
    "}\n",
    "\n",
    "main()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1072a9d5-14fc-4fdc-8ca5-35026c3d3416",
   "metadata": {},
   "source": [
    "✅ 15. 時間 time 套件"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "441c14d8-1e5c-42ab-ba99-fb9ec5dd5d20",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "現在時間: 2025-04-10 06:35:59\n",
      "兩小時後: 2025-04-10 08:35:59.825393043 +0000 UTC m=+7677.011829721\n"
     ]
    }
   ],
   "source": [
    "package main\n",
    "import (\n",
    "    \"fmt\"\n",
    "    \"time\"\n",
    ")\n",
    "\n",
    "func main() {\n",
    "    now := time.Now()\n",
    "    fmt.Println(\"現在時間:\", now.Format(\"2006-01-02 15:04:05\"))\n",
    "\n",
    "    future := now.Add(time.Hour * 2)\n",
    "    fmt.Println(\"兩小時後:\", future)\n",
    "}\n",
    "main()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Go",
   "language": "go",
   "name": "gophernotes"
  },
  "language_info": {
   "codemirror_mode": "",
   "file_extension": ".go",
   "mimetype": "",
   "name": "go",
   "nbconvert_exporter": "",
   "pygments_lexer": "",
   "version": "go1.22.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
