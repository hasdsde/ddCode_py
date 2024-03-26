## DDCode-基于TailwindCss的代码生成系统-Python端

### 主要功能

- 基于树状图、符合程序员逻辑
- 使用TailwindCss，不再写CSS
- 基于Node服务器对本地文件读取，直接渲染页面
- 读取代码，自动识别分类变量、函数、引入
- 使用Quasar框架，支持开箱即用图标、组件更丰富

### 系统功能

- 基本权限管理功能
- Material Icon速览
- 读取Swagger结构体，快速生成表格和示例数据
- Echart基本功能生成、在线预览
- 前后端菜单交互，用户登录

## 预览

登录页

![https://raw.githubusercontent.com/hasdsde/img_bed/main/QQ%E6%88%AA%E5%9B%BE20240326203612.png](https://raw.githubusercontent.com/hasdsde/img_bed/main/QQ%E6%88%AA%E5%9B%BE20240326203612.png)

管理页面

![https://raw.githubusercontent.com/hasdsde/img_bed/main/QQ%E6%88%AA%E5%9B%BE20240326203637.png](https://raw.githubusercontent.com/hasdsde/img_bed/main/QQ%E6%88%AA%E5%9B%BE20240326203637.png)

![https://raw.githubusercontent.com/hasdsde/img_bed/main/QQ%E6%88%AA%E5%9B%BE20240326203657.png](https://raw.githubusercontent.com/hasdsde/img_bed/main/QQ%E6%88%AA%E5%9B%BE20240326203657.png)

![https://raw.githubusercontent.com/hasdsde/img_bed/main/QQ%E6%88%AA%E5%9B%BE20240326203857.png](https://raw.githubusercontent.com/hasdsde/img_bed/main/QQ%E6%88%AA%E5%9B%BE20240326203857.png)

代码生成器

![https://raw.githubusercontent.com/hasdsde/img_bed/main/QQ%E6%88%AA%E5%9B%BE20240326203718.png](https://raw.githubusercontent.com/hasdsde/img_bed/main/QQ%E6%88%AA%E5%9B%BE20240326203718.png)

![https://raw.githubusercontent.com/hasdsde/img_bed/main/QQ%E6%88%AA%E5%9B%BE20240326203735.png](https://raw.githubusercontent.com/hasdsde/img_bed/main/QQ%E6%88%AA%E5%9B%BE20240326203735.png)

![https://raw.githubusercontent.com/hasdsde/img_bed/main/QQ%E6%88%AA%E5%9B%BE20240326203752.png](https://raw.githubusercontent.com/hasdsde/img_bed/main/QQ%E6%88%AA%E5%9B%BE20240326203752.png)

![https://raw.githubusercontent.com/hasdsde/img_bed/main/QQ%E6%88%AA%E5%9B%BE20240326203811.png](https://raw.githubusercontent.com/hasdsde/img_bed/main/QQ%E6%88%AA%E5%9B%BE20240326203811.png)

![https://raw.githubusercontent.com/hasdsde/img_bed/main/QQ%E6%88%AA%E5%9B%BE20240326203829.png](https://raw.githubusercontent.com/hasdsde/img_bed/main/QQ%E6%88%AA%E5%9B%BE20240326203829.png)

### 使用到的技术

``` sh
#ORM框架
pip install SQLAlchemy
#框架
pip install flask
#逆向工程
pip install sqlacodegen
#sql    
pip install pymysql
#swagger
pip install flasgger
```

### 配置

- 数据库配置 config.py
- swagger配置 routes/__init__.py

### 地址

- 后台端口：5000
- Swagger地址：http://localhost:5000/apidocs/#/

