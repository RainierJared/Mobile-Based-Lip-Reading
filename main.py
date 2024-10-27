from View.view import webServer

if __name__ == '__main__':
    pwa = webServer('MLR',template_folder='./templates')
    pwa.run(host='localhost', port='8000', debug=True)
