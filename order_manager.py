import json
INPUT_FILE = "orders.json"
OUTPUT_FILE = "output_orders.json"
x=0
print("python order_manager.py")
a={}
try:
    with open(INPUT_FILE, 'r', encoding='UTF-8') as f:
        a = json.load(f)
except:
    pass
td={}
ss=0
tdd={}
tl=[]
tp="X"
while x!='4':
    try:
        print("***************選單***************")
        print("1. 新增訂單")
        print("2. 顯示訂單報表")
        print("3. 出餐處理")
        print("4. 離開")
        print("**********************************")
        x=input("請選擇操作項目(Enter 離開)：")
        if x=='1':
            td={}
            tl=[]
            tp="x"
            td["order_id"]=input("請輸入訂單編號：").upper()
            for i in range(0,len(a)) :
                if td["order_id"]==a[i]["order_id"]:
                    print("錯誤：訂單編號 "+td["order_id"]+" 已存在！")
                    tp="o"
                    break
            if tp=="o":
                continue
            td["customer"]=input("請輸入顧客姓名：")
            while tp!="":
                tp=input("請輸入訂單項目名稱（輸入空白結束）：")
                tdd={}
                tdd["name"]=tp
                if tp!="":
                    tp=input("請輸入價格：")
                    try:
                        if int(tp)<0:
                            print("錯誤：價格不能為負數，請重新輸入")
                            continue
                    except:
                        pass
                    if tp.isdigit()==0:
                        print("錯誤：價格或數量必須為整數，請重新輸入")
                        continue
                    tdd["price"]=int(tp)
                    tp=input("請輸入數量：")
                    try:
                        if int(tp)<=0:
                            print("錯誤：數量必須為正整數，請重新輸入")
                            continue
                    except:
                        pass
                    if tp.isdigit()==0:
                        print("錯誤：價格或數量必須為整數，請重新輸入")
                        continue
                    tdd["quantity"]=int(tp)
                    tl.append(tdd)
            if tl==[]:
                print("至少需要一個訂單項目")
                continue
            td["items"]=tl
            a.append(td)
        elif x=='2':
            td={}
            for i in range(0,len(a)) :
                ss=0
                print()
                print("==================== 訂單報表 ====================")
                print("訂單 #"+str(i+1))
                print("訂單編號: "+str(a[i]["order_id"]))
                print("客戶姓名: "+str(a[i]["customer"]))
                print("--------------------------------------------------")
                print(f"{'商品名稱':{chr(12288)}<10}{'單價':{chr(12288)}<10}{'數量':{chr(12288)}<10}{'小計':{chr(12288)}<10}")
                print("--------------------------------------------------")
                td=a[i]["items"]
                for l in range(0,len(td)) :
                    ss=ss+td[l]["price"]*td[l]["quantity"]
                    print(f"{td[l]['name']:{chr(12288)}<10}{td[l]['price']:{chr(12288)}<10}{td[l]['quantity']:{chr(12288)}<10}{str(td[l]['price'] * td[l]['quantity']):{chr(12288)}<10}")
                print("--------------------------------------------------")
                print("訂單總額: "+str(ss))
                print("==================================================")
        elif x=='3':
            ss=0
            print()
            print("======== 待處理訂單列表 ========")
            for i in range(0,len(a)) :
                print("訂單編號: "+a[i]["order_id"]+" - 客戶: "+a[i]["customer"])
            print("================================")
            tp="a"
            while tp=="a":
                tp=input("請選擇要出餐的訂單編號 (輸入數字或按 Enter 取消):")
                if tp=="":
                    break
                if tp.isdigit()==0:
                    print("錯誤：請輸入有效的數字")
                    tp="a"
            if tp!="":
                td=a[int(tp)-1]
                with open(OUTPUT_FILE, 'w', encoding='UTF-8') as f:
                     json.dump( td, f, ensure_ascii=False, indent=4)
                print("訂單 O002 已出餐完成")
                print("出餐訂單詳細資料：")
                print()
                print("==================== 出餐訂單 ====================")
                print("訂單編號: "+td["order_id"])
                print("客戶姓名: "+td["customer"])
                print("--------------------------------------------------")
                print(f"{'商品名稱':{chr(12288)}<10}{'單價':{chr(12288)}<10}{'數量':{chr(12288)}<10}{'小計':{chr(12288)}<10}")
                print("--------------------------------------------------")
                td=a[i]["items"]
                for l in range(0,len(td)) :
                    ss=ss+td[l]["price"]*td[l]["quantity"]
                    print(f"{td[l]['name']:{chr(12288)}<10}{td[l]['price']:{chr(12288)}<10}{td[l]['quantity']:{chr(12288)}<10}{str(td[l]['price'] * td[l]['quantity']):{chr(12288)}<10}")
                print("--------------------------------------------------")
                print("訂單總額: "+str(ss))
                print("==================================================")
        elif x!='4':
            print("請輸入有效的選項（1-4）")
    except:
        print("發生錯誤")
