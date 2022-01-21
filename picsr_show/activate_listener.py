"""程序被激活的入口以及监控调用下一步显示"""
from pynput.keyboard import Key, Controller, Listener
import picsr_show



class Main:
    """主类"""
    def __init__(self):
        """主函数"""
        # 激活截图，使用无敌简洁的写法，完美！！！
        controller = Controller()
        with controller.pressed(Key.cmd):
            with controller.pressed(Key.shift):
                controller.press('s')
                controller.release('s')
        # 监控enter键，检查到就激活图片处理
        # 设定监听，卡住程序，如果出现enter，就将监听线程停掉继续后面的操作
        with Listener(
                on_press=self.on_press, on_release=self.on_release
        ) as self.listener:
            self.listener.join()
        # 激活图片显示
        picsr_show.main()

    def on_press(self, key):
        """按键按下响应"""
        # 停掉监听线程，进行后面的操作
        self.listener.stop()

    def on_release(self, key):
        """按键松开响应"""
        pass


if __name__ == '__main__':
    Main()
