create table menu
(
    id           int auto_increment
        primary key,
    url          varchar(40)  null comment 'URL',
    name         varchar(40)  null,
    parent_id    int          null,
    authority_id int          null,
    orders       int          null comment '排序，越高越靠前',
    icon         varchar(100) null
);

create index menu_authority_id_fk
    on menu (authority_id);

INSERT INTO ddpy.menu (id, url, name, parent_id, authority_id, orders, icon) VALUES (1, '/dashboard', '仪表盘', null, null, 2, 'dashboard');
INSERT INTO ddpy.menu (id, url, name, parent_id, authority_id, orders, icon) VALUES (2, '/sys', '系统管理', null, null, 2, 'settings');
INSERT INTO ddpy.menu (id, url, name, parent_id, authority_id, orders, icon) VALUES (3, '/front', '前端工具', null, null, 2, 'auto_fix_high');
INSERT INTO ddpy.menu (id, url, name, parent_id, authority_id, orders, icon) VALUES (5, '/dashboard/home', '首页', 1, null, 1, 'grid_view');
INSERT INTO ddpy.menu (id, url, name, parent_id, authority_id, orders, icon) VALUES (6, '/sys/user', '用户管理', 2, null, 1, 'account_circle');
INSERT INTO ddpy.menu (id, url, name, parent_id, authority_id, orders, icon) VALUES (9, '/sys/menu', '菜单管理', 2, null, 1, 'list');
INSERT INTO ddpy.menu (id, url, name, parent_id, authority_id, orders, icon) VALUES (10, '/front/tailwind', 'Tailwind生成器', 3, null, 2, 'cyclone');
INSERT INTO ddpy.menu (id, url, name, parent_id, authority_id, orders, icon) VALUES (11, '/front/icon', 'Material Icon 列表', 3, null, 1, 'emoji_events');
INSERT INTO ddpy.menu (id, url, name, parent_id, authority_id, orders, icon) VALUES (12, '/front/func', '函数调用指南', 3, null, 1, 'functions');
INSERT INTO ddpy.menu (id, url, name, parent_id, authority_id, orders, icon) VALUES (13, '/front/table', '表格配置工具', 3, null, 1, 'insert_chart_outlined');
INSERT INTO ddpy.menu (id, url, name, parent_id, authority_id, orders, icon) VALUES (17, '/front/echart', 'Echarts生成器', 3, null, 1, 'donut_large');

create table user
(
    id        int auto_increment comment '主键'
        primary key,
    user_name varchar(40)  null comment '登录名',
    nick_name varchar(40)  null comment '显示名称',
    email     varchar(100) null comment '邮箱',
    phone     varchar(20)  null comment '手机号',
    sex       int          null comment '性别 0-未知 1男 2女',
    avatar    varchar(200) null comment '头像',
    password  varchar(40)  null comment '密码',
    comment   varchar(100) null comment '备注'
)
    comment '用户表';

INSERT INTO ddpy.user (id, user_name, nick_name, email, phone, sex, avatar, password, comment) VALUES (1, 'zhangsan', '张三', 'zhangsan@qq.com', '17565286323', 1, null, 'E10ADC3949BA59ABBE56E057F20F883E', null);
INSERT INTO ddpy.user (id, user_name, nick_name, email, phone, sex, avatar, password, comment) VALUES (2, 'admin', 'adminssss', '114514191810@qq.com', '1145141919810', 0, '', 'E10ADC3949BA59ABBE56E057F20F883E', '最高の管理员');
INSERT INTO ddpy.user (id, user_name, nick_name, email, phone, sex, avatar, password, comment) VALUES (3, 'lisi', '李四', '123', '123', 1, '', '', '');
