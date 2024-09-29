import cv2
import numpy as np

# 画像の読み込み
image = cv2.imread('./latest_foF2.jpg')

# BGRからHSVに変換
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 赤色の範囲を指定してマスクを作成
lower_red = np.array([0, 50, 50])
upper_red = np.array([10, 255, 255])
mask1 = cv2.inRange(hsv_image, lower_red, upper_red)

lower_red2 = np.array([170, 50, 50])
upper_red2 = np.array([180, 255, 255])
mask2 = cv2.inRange(hsv_image, lower_red2, upper_red2)

# マスクを合成
mask = mask1 + mask2

# 赤いプロットのみを抽出
red_points = cv2.bitwise_and(image, image, mask=mask)

# 赤いプロットの座標を取得
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 各プロットの座標をリストに格納
plot_coords = []
for contour in contours:
    # 各プロットの重心を計算して座標を取得
    M = cv2.moments(contour)
    if M["m00"] != 0:
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])
        plot_coords.append((cx, cy))

# 座標を表示
print(plot_coords)

# 赤いプロットを強調表示
for coord in plot_coords:
    cv2.circle(image, coord, 5, (0, 255, 0), -1)

# 結果の画像を保存
cv2.imwrite('highlighted_red_points.jpg', image)
