with open('source.txt','r',encoding='utf-8') as source_file,\
     open('target.txt','w',encoding='utf-8') as target_file:
    for line in source_file:
        target_file.write(line)
print("复制完成！")