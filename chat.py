#讀取檔案
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding = 'utf-8-sig') as f:
        #-sig要去掉文件一開始的'\ufeff'
        for line in f:
            lines.append(line.strip())
        return lines

def convert(lines):
    new = []
    person = None  #預設直設為無
    for line in lines:
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue
        if person: #如果person有值就執行下面程序
            new.append(person + ': ' + line)
    return new

def write_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')

def main():
    lines = read_file('input.txt')
    lines = convert(lines) #丟lines進去用新的lines覆蓋
    write_file('output.txt', lines)

main()
    