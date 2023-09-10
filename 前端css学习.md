css三种定义方式

**内联方式**

 <div style





**head里编写方式**

![image-20230305112516384](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230305112516384.png)



**引入css文件方式**（常用）



按理解来看，css的存在其实就是将内容与渲染、排布【隔离】

通过一个css文件统一管理，利用css选择器，去映射html中的某个元素，并加入其属性

最终考虑的其实是抽象(提取) 与 设计



### css选择器

#### 类选择器

![image-20230305130807802](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230305130807802.png)



![image-20230305130825425](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230305130825425.png)

.class {

}

css中利用.  进行定位

注：系统css中可以共一个css中的选择属性

1.html css 多对一

2.在一个元素中可多个引用css

![image-20230305131442431](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230305131442431.png)



![image-20230305131455037](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230305131455037.png)

空格分隔 两个类



#### id选择器

#id {

}

id在每个页面中 仅存在一个(约定) 身份证

注：id无法解析类似于class中中间的空格



### 全局配置器

*{

}

通配



整体：

![image-20230305140416248](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230305140416248.png)

![image-20230305141103224](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230305141103224.png)









# css三大特性

![image-20230305143052994](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230305143052994.png)

![image-20230305143230503](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230305143230503.png)



![image-20230305143354107](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230305143354107.png)





