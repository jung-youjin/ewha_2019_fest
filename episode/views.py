from django.shortcuts import render, get_object_or_404, redirect

from .models import Board, Comment

from django.utils import timezone

# from django.core.urlresolvers import reverse_lazy

# Create your views here.

def home(request):
    boards = Board.objects
    return render(request, 'home.html', {'boards': boards})

def detail(request, board_id):
    board_detail = get_object_or_404(Board, pk=board_id)
    return render(request, 'detail.html', {'board': board_detail})

def new(request):
    return render(request, 'new.html')

def create(request):
    board = Board()
    board.title = request.GET['title']
    board.body = request.GET['body']
    board.pub_date = timezone.datetime.now()
    board.save()
    return redirect('/myapp/' + str(board.id))

def delete(request, board_id):
    board = Board.objects.get(pk = board_id)
    board.delete()
    return redirect('/')

def edit(request, board_id):
    board_edit = Board.objects.get(pk= board_id)
    return render(request, 'edit.html', {'board': board_edit})

def update(request, board_id):
    board = Board.objects.get(pk= board_id)
    board.title = request.POST['title']
    board.body = request.POST['body']
    board.pub_date = timezone.datetime.now()
    board.save()
    return redirect('/')

def comment_write(request, board_id):
    if request.method == 'POST':
        post = get_object_or_404(Board, pk=board_id)
        content = request.POST.get('content')
        drop = request.POST.get('crowded')
        print(drop)

    if not content:
        messages.info(request, 'You didnt write anything')
        return redirect('detail', board_id)

    Comment.objects.create(post=post, comment_contents=content, dropdown=drop)
    return redirect('detail', board_id)

def board_search(request):
    keyword = request.GET.get('board_search')
    results = Board.objects.filter(title__contains = keyword)
    
    return render(request, 'search_result.html',{'results':results, 'keyword':keyword})

def event(request):
    return render(request, "event.html")

# Create your views here.
