import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# 画像を読み込む
img_path = './latest_foF2.jpg'  # 画像ファイルのパス
img = mpimg.imread(img_path)

# クリックした座標を格納するリスト
click_coords = []

# クリックイベントを処理する関数
def onclick(event):
    if event.xdata is not None and event.ydata is not None:  # 座標が有効な場合
        # クリックした座標をリストに追加
        click_coords.append((event.xdata, event.ydata))
        print(f'Clicked coordinates: ({event.xdata}, {event.ydata})')

# 画像を表示
fig, ax = plt.subplots()
ax.imshow(img)

# マウスクリックイベントをバインド
cid = fig.canvas.mpl_connect('button_press_event', onclick)

# プロットを表示し、クリックを待つ
plt.show()

# クリックした座標を表示
print("All clicked coordinates:", click_coords)
