+ 方法`findViewById()`获取布局文件中控件的实例，Kotlin可使用插件来根据布局文件中定义的空间id自动生成一个具有相同名称的变量，可在Activity中直接使用这个变量

  > P92

  1. 在`build.gradle`中的`plugins`（在文件首）添加`id 'kotlin-android-extensions'`
  2. sync now
  3. 在activity中import进`import kotlinx.android.synthetic.main.那个layout.*`（建议使用补全）

+ 创建了两个按钮，但是按钮重叠，在Design中拖动

  但是拖动后编译运行后两个按钮仍然重叠

  > P92

  0. 观察当前layout的xml文件，Code的前面，有

     ```kotlin
     <android.constraintlayout.widget...
     ```

     说明这是一个约束布局

  1. 点击一个按钮，悬停其上，其四个边有圆形，按住正对另一个按钮的圆形，拖动（动画是箭头）到相对的按钮上，再次运行则可行

  + 两个按钮相对整个屏幕也是这样的，将一个圆形拖动到屏幕边界
  + 通过圆圈连接后，是确定约束关系，相对位置仍然可以调整
