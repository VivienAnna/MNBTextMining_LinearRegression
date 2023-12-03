import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

# Data import
df_BUX = pd.read_csv('../Ratios/Bux_ratio_neg_1.csv', sep=';')
df_RATIO = pd.read_csv('../Ratios/ratio.csv', sep=';')

x_RATIO= df_RATIO[['Positive','Negative']]
y1_BUX=df_BUX['rateRatio']

# Visualisation RATIO-BUX
# X and Y values preparation for regression
X = df_RATIO[['Positive', 'Negative']].values.reshape(-1,2)
Y = df_BUX['rateRatio']

# Prepare model data point for visualization
x = X[:, 0]
y = X[:, 1]
z = Y

#
x_pred = np.linspace(0, 1, 30)      # range of ratio values
y_pred = np.linspace(0, 2, 30)  # range of BUX values
xx_pred, yy_pred = np.meshgrid(x_pred, y_pred)
model_viz = np.array([xx_pred.flatten(), yy_pred.flatten()]).T

# Train
ols = linear_model.LinearRegression()
model = ols.fit(X, Y)
predicted = model.predict(model_viz)

# Evaluate
r2 = model.score(X, Y)

#Plot
plt.style.use('default')
fig = plt.figure(figsize=(12, 4))

# 3D plot
ax1 = fig.add_subplot(131, projection='3d')
ax2 = fig.add_subplot(132, projection='3d')
ax3 = fig.add_subplot(133, projection='3d')

axes = [ax1, ax2, ax3]

for ax in axes:
    ax.plot(x, y, z, color='k', zorder=15, linestyle='none', marker='o', alpha=0.5)
    ax.scatter(xx_pred.flatten(), yy_pred.flatten(), predicted, facecolor=(0,0,0,0), s=20, edgecolor='#70b3f0')
    ax.set_xlabel('Positive', fontsize=12)
    ax.set_ylabel('Negative', fontsize=12)
    ax.set_zlabel('RateRatio', fontsize=12)
    ax.locator_params(nbins=4, axis='x')
    ax.locator_params(nbins=5, axis='x')

ax1.text2D(0.2, 0.32, 'BUX', fontsize=13, ha='center', va='center',
           transform=ax1.transAxes, color='grey', alpha=0.5)
ax2.text2D(0.3, 0.42, 'BUX', fontsize=13, ha='center', va='center',
           transform=ax2.transAxes, color='grey', alpha=0.5)
ax3.text2D(0.85, 0.85, 'BUX', fontsize=13, ha='center', va='center',
           transform=ax3.transAxes, color='grey', alpha=0.5)

ax1.view_init(elev=27, azim=112)
ax2.view_init(elev=16, azim=-51)
ax3.view_init(elev=60, azim=165)

fig.suptitle('BUX-RATIO $R^2 = %.2f$' % r2, fontsize=20)

fig.tight_layout()
plt.show()

# GIF
fig2= plt.figure(figsize=(12, 4))

ax_single=fig2.add_subplot(111, projection='3d')

ax_single.plot(x, y, z, color='k', zorder=15, linestyle='none', marker='o', alpha=0.5)
ax_single.scatter(xx_pred.flatten(), yy_pred.flatten(), predicted, facecolor=(0,0,0,0), s=20, edgecolor='#70b3f0')
ax_single.set_xlabel('Positive', fontsize=12)
ax_single.set_ylabel('Negative', fontsize=12)
ax_single.set_zlabel('RateRatio', fontsize=12)
ax_single.locator_params(nbins=4, axis='x')
ax_single.locator_params(nbins=5, axis='x')

ax_single.text2D(0.3, 0.42, 'BUX', fontsize=13, ha='center', va='center',
           transform=ax_single.transAxes, color='grey', alpha=0.5)

for ii in np.arange(0, 360, 1):
    ax_single.view_init(elev=16, azim=ii)
    fig2.savefig('BUX_gif_image%d.png' % ii)