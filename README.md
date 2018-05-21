#简单的工资计算器

##csv文件的操作
读取所有行数据， 汇总成一个list
list(csv.reader(f))

写入
csv.writer(f).writerow([...]) 一个list
