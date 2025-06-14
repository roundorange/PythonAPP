import traceback

if __name__ == '__main__':
    try:
        from appsrc import MainWidget
        MainWidget().run()
    except:
        ret = traceback.format_exc()
        print(ret)

