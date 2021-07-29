#讀取檔案
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding = 'utf-8-sig') as f:
        #-sig要去掉文件一開始的'\ufeff'
        for line in f:
            lines.append(line.strip())
        return lines

def convert(lines):
    person = None  #預設直設為無
    allen_word_count = 0
    viki_word_count = 0
    allen_sticker_count = 0
    viki_sticker_count = 0
    allen_image_count = 0
    viki_image_count = 0
    for line in lines:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
                allen_sticker_count += 1
            elif s[2] == '圖片':
                allen_image_count += 1
            else:
                for m in s[2:]:
                    allen_word_count += len(m)
        elif name == 'Viki':
            if s[2] == '貼圖':
                viki_sticker_count += 1
            elif s[2] == '圖片':
                viki_image_count += 1
            else:
                for m in s[2:]:
                    viki_word_count += len(m)
    print('allen_say', allen_word_count)
    print('viki_say', viki_word_count)  
    print('allen_used', allen_sticker_count, 'times')   
    print('viki_used', viki_sticker_count, 'times')
    print(allen_image_count)
    print(viki_image_count)

def write_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')

def main():
    lines = read_file('LINE-Viki.txt')
    lines = convert(lines) #丟lines進去用新的lines覆蓋
    #write_file('output2.txt', lines)

main()
    