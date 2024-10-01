import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import datetime
import math

# 画像を読み込む
img_path = './latest_tec.jpg'
img = mpimg.imread(img_path)

# グラフのデータ (例として)
graphs = {
    '45°N': {
        'position': [78.27230682986084, 56.908950761468645, 850, 172.22241427637107],  # 画像におけるグラフの左上(x,y)と右下(x,y)の座標
    },
    '41°N': {
        'position': [78.27230682986084, 174.12842193777442, 850, 289.44188545267673],  # 例として別のグラフの位置
    },
    '37°N': {
        'position': [78.27230682986084, 291.3478931140801, 850, 407.6143604596842],  # 例として別のグラフの位置
    },
    '33°N': {
        'position': [78.27230682986084, 409.52036812108753, 850, 524.8338316359899],  # 例として別のグラフの位置
    },
    '29°N': {
        'position': [78.27230682986084, 526.7398392973932, 850, 642.0533028122957],  # 例として別のグラフの位置
    }
}

# 時間範囲（例として仮定）
#start_time = datetime.datetime(2024, 9, 23)
#end_time = datetime.datetime(2024, 9, 28)
#time_range = (end_time - start_time).total_seconds()

# 日数範囲の設定（例として1日目から6日目）
days_range = 6

# y軸の範囲（TECの値の範囲）
y_min = 0
y_max = 150

click_coords = []

fig, ax = plt.subplots()
ax.imshow(img)

def onclick(event):
    if event.xdata is not None and event.ydata is not None:
        click_coords.append((event.xdata, event.ydata))
        for name, graph in graphs.items():
            pos = graph['position']
            if pos[0] <= event.xdata <= pos[2] and pos[1] <= event.ydata <= pos[3]:
                #x_ratio = (event.xdata - pos[0]) / (pos[2] - pos[0])
                x_ratio = (event.xdata - pos[0]) / (pos[2] - pos[0])
                y_ratio = 1 - (event.ydata - pos[1]) / (pos[3] - pos[1])  # y軸は上から下に向かって増加するため逆にする
                
                #clicked_time = start_time + datetime.timedelta(seconds=x_ratio * time_range)
                clicked_day = math.floor(1 + x_ratio * days_range)
                clicked_value = round(y_min + y_ratio * (y_max - y_min))
                
                
                # print(f'Clicked on {name} graph: Time: {clicked_time}, Value: {clicked_value}')
                print(f'Clicked on {name} graph: Day: {clicked_day}, Value: {clicked_value}')
                
                # クリックした位置に青い点をプロット
                ax.plot(event.xdata, event.ydata, marker='o', markersize=3, color='blue', mfc='none') 
                # 補助線を引く（垂直線と水平線）
                #ax.axvline(event.xdata, color='blue', linestyle='--', linewidth=1)
                #ax.axhline(event.ydata, color='blue', linestyle='--', linewidth=1)
                
                # 座標表示
                #ax.text(event.xdata + 10, event.ydata + 10, f'Time: {clicked_time}\nValue: {clicked_value:.2f}', color='blue', fontsize=5) 
                ax.text(event.xdata + 10, event.ydata + 10, f'Day: {clicked_day}\nValue: {clicked_value:.2f}', color='blue', fontsize=5) 
                fig.canvas.draw()

                break
        else:
            print(f'Clicked coordinates: ({event.xdata}, {event.ydata})')

cid = fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()
#print("All clicked coordinates:", click_coords)
