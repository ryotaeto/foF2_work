import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import datetime

# 画像を読み込む
img_path = './latest_foF2.jpg'
img = mpimg.imread(img_path)

# グラフのデータ (例として)
graphs = {
    'Wakkanai': {
        'position': [78.27230682986084, 60.72096608427535, 850, 203.6715406895263],  # 画像におけるグラフの左上(x,y)と右下(x,y)の座標
    },
    'Kokubunji': {
        'position': [78.27230682986084, 206.53055218163126, 850, 350.43413061758383],  # 例として別のグラフの位置
    },
    'Yamagawa': {
        'position': [78.27230682986084, 352.3401382789872, 850, 496.2437167149397],  # 例として別のグラフの位置
    },
    'Okinawa': {
        'position': [78.27230682986084, 498.14972437634304, 850, 642.0533028122957],  # 例として別のグラフの位置
    }
}

# 時間範囲（例として仮定）
start_time = datetime.datetime(2024, 9, 23)
end_time = datetime.datetime(2024, 9, 28)
time_range = (end_time - start_time).total_seconds()

# y軸の範囲（foF2の値の範囲）
y_min = 2
y_max = 22

click_coords = []

fig, ax = plt.subplots()
ax.imshow(img)

def onclick(event):
    if event.xdata is not None and event.ydata is not None:
        click_coords.append((event.xdata, event.ydata))
        for name, graph in graphs.items():
            pos = graph['position']
            if pos[0] <= event.xdata <= pos[2] and pos[1] <= event.ydata <= pos[3]:
                x_ratio = (event.xdata - pos[0]) / (pos[2] - pos[0])
                y_ratio = 1 - (event.ydata - pos[1]) / (pos[3] - pos[1])  # y軸は上から下に向かって増加するため逆にする
                
                clicked_time = start_time + datetime.timedelta(seconds=x_ratio * time_range)
                clicked_value = round(y_min + y_ratio * (y_max - y_min) ,1)
                
                
                print(f'Clicked on {name} graph: Time: {clicked_time}, Value: {clicked_value}')
                
                # クリックした位置に青い点をプロット
                ax.plot(event.xdata, event.ydata, marker='o', markersize=3, color='blue', mfc='none') 
                # 補助線を引く（垂直線と水平線）
                #ax.axvline(event.xdata, color='blue', linestyle='--', linewidth=1)
                #ax.axhline(event.ydata, color='blue', linestyle='--', linewidth=1)
                
                # 座標表示
                ax.text(event.xdata + 10, event.ydata + 10, f'Time: {clicked_time}\nValue: {clicked_value:.2f}', color='blue', fontsize=5) 
                fig.canvas.draw()

                break
        else:
            print(f'Clicked coordinates: ({event.xdata}, {event.ydata})')

cid = fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()
print("All clicked coordinates:", click_coords)
