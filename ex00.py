class CSV:
    def __init__(self,filename,postfix,is_head):
        self.filename=filename
        self.postfix=postfix
        self.is_head=is_head

    def is_csv(self):
         d=self.filename
         b="csv"
         if len(d and b )> 2:
             return True
         else:
             return Flase

    def is_head(self):
        csvfile=open(filename,"r")
        a=csvfile.read(0)
        arr=a.split()
        b=arr[0]
        n=["Name","Age","No"]
        if len(a and n) > 0:
            return True
        else:
            return Flase

    def read(self):
        if self.is_csv():
            if self.is_head:
                csvfile=open(self.filename,"r")
                a=csvfile.read()
                arr=a.split()
                for t in arr:
                    print(t)
            else:
                print("只能处理带头部文件")
        else:
            print("只能处理.csv后缀文件")

csv=CSV("ex0_sample.csv","csv",True)
csv.read()
