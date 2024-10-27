from view import webServer

if __name__ == '__main__':
    pwa = webServer('MLR',template_folder='./templates')
    pwa.run(host='192.168.1.32', port='8000', debug=True)