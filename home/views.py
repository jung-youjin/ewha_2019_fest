from django.shortcuts import render
from .models import Fest, Board, Comment
import csv
import datetime

# Create your views here.

def home(request): #메인화면
    return render(request, 'index.html')

def first(request): #첫날
    try:
        place = request.GET['place']
    except :
        place = "hak"
    booths = Fest.objects.filter(place = place).filter(date = 1).order_by('booth_num')
    return render(request, 'first.html', {'booths':booths, 'place':place})

def second(request): #둘째날
    try:
        place = request.GET['place']
    except :
        place = "hak"
    booths = Fest.objects.filter(place = place).filter(date = 2).order_by('booth_num')
    return render(request, 'second.html', {'booths':booths, 'place':place})

def third(request): #셋째날
    try:
        place = request.GET['place']
    except :
        place = "hak"
    booths = Fest.objects.filter(place = place).filter(date = 3).order_by('booth_num')
    return render(request, 'third.html', {'booths':booths, 'place':place})

def import_fest(request): #csvimport하는 함수
    with open("ewhafest1.csv") as f: #csv파일 열기
        reader = csv.reader(f) #reader함수 : iterator타입 reader 객체 return
        i = 0
        for row in reader: #한 행씩 접근
            if(row[0] == '888888'):
                break
            fest = Fest() #모델
            if(row[0] == ''):
                fest.date = -1
            else :
                fest.date = int(row[0])

            if(row[1] == ''):
                fest.place = -1
            else :
                fest.place = row[1]

            if(row[2] == ''):
                fest.booth_num = -1
            else :
                fest.booth_num = int(row[2])

            if(row[3] == ''):
                fest.name = -1
            else : fest.name = row[3]

            if(row[4] == ''):
                fest.sold_out = -1
            else : fest.sold_out = int(row[4])

            if(row[5] == ''):
                fest.password = -1
            else :
                fest.password = int(row[5])
            fest.detail = row[6]
            fest.save()

    return redirect('home')

def search(request): #검색
    try :
        kind = request.GET['kind']
        keyword = request.GET['search']
        date = request.GET['date']
    except :
        kind = request.GET['kind']
        keyword = request.GET['search']
        date = "none"

    if(kind == "name"):
        results = Fest.objects.filter(name__contains = keyword)
    else :
        results = Fest.objects.filter(detail__contains = keyword)
    return render(request, 'search.html', {'results':results, 'kind':kind, 'keyword':keyword, 'date':date})

def sold_out(request):
    password = request.GET['password']
    now = datetime.datetime.now().day
    if(now==15):
        password_match = Fest.objects.filter(password=password).filter(date=1)
        for i in password_match:
            if(i.sold_out == 0):
                i.sold_out=1
                i.save()
            else:
                i.sold_out=0
                i.save()
    elif(now==16):
        password_match = Fest.objects.filter(password=password).filter(date=2)
        for i in password_match:
            if(i.sold_out == 0):
                i.sold_out=1
                i.save()
            else:
                i.sold_out=0
                i.save()
    else:
        password_match = Fest.objects.filter(password=password).filter(date=3)
        for i in password_match:
            if(i.sold_out == 0):
                i.sold_out=1
                i.save()
            else:
                i.sold_out=0
                i.save()
    #password_match = Fest.objects.filter(password = password_request)
    #password_match = Fest.objects.filter(password=password)
    #if(password_match.sold_out == '0'):
    #    password_match.sold_out == '1'
    #    password_match.save()
    #else:
    #    password_match.sold_out == '0'
    #    password_match.save()
    return render(request, 'sold_out.html', {'password_match':password_match, 'password':password, 'now':now})
    #password_request = request.POST['password']
    #passwords = Fest.objects.filter(password_request=password)
    #if(fest.sold_out == '1'):
    #    fest.sold_out = '0'
    #else:
    #    fest.sold_out = '1'
    #fest.save()
    #return render(request, 'index.html', fest.password)

def board(request):
    boards = Board.objects
    booths = Fest.objects
    return render(request, 'board.html', {'boards':boards, 'booths':booths})

def comment_write(request):
    board = Board()
    board.title = request.GET['title']
    board.body = request.GET['body']
    board.pub_date = timezone.datetime.now()
    board.save()
    return redirect('/board.html')
