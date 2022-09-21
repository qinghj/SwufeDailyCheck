## 用 github actions 实现每日定时打卡

### 如何使用？

1. 在GitHub上fork[仓库](https://github.com/qinghj/SwufeDailyCheck)
2. 在fork的仓库中点击Actions，选择启用 github actions
3. 每天八点半自动打卡；star一下fork的仓库(yourusername/SwufeDailyCheck)可以手动执行action
4. 失败github会有邮件提示

--------------------

使用 python selenium，github actions 需要安装chrome, chromedriver, python 等依赖（见.github/workflows/main.yml)，
速度缓慢

欢迎改进