import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Specific player replacements with mvpBonus and dynasty
# Format: (player_name, mvpBonus, dynasty)
player_fixes = [
    # Three-peat MVPs (bonus=2)
    ("比尔-拉塞尔", 2, 1),
    ("威尔特-张伯伦", 2, 0),
    ("拉里-伯德", 2, 1),
    
    # Michael Jordan: 1991-92 back-to-back + 1996-98 three-peat, bonus=3
    ("迈克尔-乔丹", 3, 1),
    
    # Back-to-back MVPs (bonus=1)
    ("勒布朗-詹姆斯", 2, 0),
    ("斯蒂芬-库里", 1, 1),
    ("扬尼斯-阿德托昆博", 1, 0),
    ("尼古拉-约基奇", 1, 0),
    ("谢伊-吉尔杰斯-亚历山大", 1, 0),
    ("史蒂夫-纳什", 1, 0),
    ("蒂姆-邓肯", 1, 1),
    ("摩西-马龙", 1, 0),
    ("魔术师约翰逊", 1, 1),
    
    # Dynasty players (dynasty=1, no MVP streak bonus)
    ("卡里姆-阿卜杜尔-贾巴尔", 0, 1),
    ("鲍勃-库西", 0, 1),
    ("约翰-哈夫利切克", 0, 1),
    ("萨姆-琼斯", 0, 1),
    ("汤姆-海因索恩", 0, 1),
    ("比尔-沙曼", 0, 1),
    ("斯科蒂-皮蓬", 0, 1),
    ("丹尼斯-罗德曼", 0, 1),
    ("詹姆斯-沃西", 0, 1),
    ("杰里-韦斯特", 0, 1),
    ("科比-布莱恩特", 0, 1),
    ("沙奎尔-奥尼尔", 0, 1),
    ("托尼-帕克", 0, 1),
    ("马努-吉诺比利", 0, 1),
    ("卡哇伊-莱昂纳德", 0, 1),
    ("凯文-杜兰特", 0, 1),
    ("克莱-汤普森", 0, 1),
    ("德雷蒙德-格林", 0, 1),
    ("安德烈-伊戈达拉", 0, 1),
    ("戴夫-考恩斯", 0, 1),
    ("凯文-麦克海尔", 0, 1),
    ("罗伯特-帕里什", 0, 1),
    ("乔治-麦肯", 0, 1),  # Early Lakers dynasty
]

for player, mvp_bonus, dynasty in player_fixes:
    pattern = 'name:"' + player + '",'
    idx = content.find(pattern)
    if idx >= 0:
        end = content.find("}", idx)
        entry = content[idx:end]
        # Fix mvpBonus
        entry = re.sub(r'mvpBonus:\d+', 'mvpBonus:' + str(mvp_bonus), entry)
        # Fix dynasty
        entry = re.sub(r'dynasty:\d+', 'dynasty:' + str(dynasty), entry)
        # Replace in content
        old_entry = content[idx:end]
        content = content[:idx] + entry + content[end:]
        print(f"Fixed: {player} (mvpBonus={mvp_bonus}, dynasty={dynasty})")
    else:
        print(f"NOT FOUND: {player}")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("\nAll fixes complete!")
