User1 = User.objects.create_user(username = 'Максим', email = 'max@mail.ru', password = 'max')

User2 = User.objects.create_user(username = 'Мария', email = 'masha@mail.ru', password = 'masha')

Author1 = Author.objects.create(user=User1)

Author2 = Author.objects.create(user=User2)

Category1 = Category.objects.create(name='Спорт')

Category2 = Category.objects.create(name='Политика')

Category3 = Category.objects.create(name='Образование')

Category4 = Category.objects.create(name='Экономика')

texttost1 = "'США могут вывести своих военных из ОАЭ и Саудовской Аравии в качестве ответной меры на решение ОПЕК+ сократить добычу нефти на два миллиона баррелей в сутки. Об этом сообщает Washington Times'"

texttost2 = "'Большинство школьников в Московской области останутся дома в период осенних каникул, сообщает интернет-издание Подмосковье сегодня. Издание проводило соответствующий опрос в соцсетях, участие приняли 200 чел'"

texttost3 = "'Решение группы ОПЕК+ сократить добычу нефти было «бесполезным и неразумным» для мировой экономики, особенно для рынков развивающихся стран. Об этом заявила министр финансов США Джанет Йеллен в интервью Financial Times'"

St1 = Post.objects.create(author = Author1, neworart = True, title = 'Месть США', text = texttost1)

St2 = Post.objects.create(author = Author2, neworart = True, title = 'Каникулы', text = texttost2)

St3 = Post.objects.create(author = Author1, neworart = False, title = 'Добыча нефти', text = texttost3)

PostCategory.objects.create(post = St1, category = Category2)

PostCategory.objects.create(post = St2, category = Category3)

PostCategory.objects.create(post = St3, category = Category2)

PostCategory.objects.create(post = St3, category = Category4)

Comment1 = Comment.objects.create(post=St1, user=User1, text='Поддерживаю данное решение')

Comment2 = Comment.objects.create(post=St2, user=User1, text='Наконец-то дети смогут отдохнуть')

Comment3 = Comment.objects.create(post=St1, user=User2, text='Хотелось бы поменьше таких происшествий')

Comment4 = Comment.objects.create(post=St3, user=User2, text='Надеюсь, это не приведёт к новому кризису')

AllPosts = [St1, St2, St3, Comment1, Comment2, Comment3, Comment4]

for i in range(100):
    target = random.choice(AllPosts)
    target.like()

for i in range(100):
    target = random.choice(AllPosts)
    target.dislaike()

Author1.update_rating()

Author2.update_rating()

lider = Author.objects.all().order_by('-rating')[0]

print(lider.user.username, lider.rating)

bestpost = Post.objects.filter(neworart=True).order_by('-rating_post')[0]

print(bestpost.time_in)
print(bestpost.author.user.username)
print(bestpost.rating_post)
print(bestpost.title)
print(bestpost.preview())

for v in Comment.objects.filter(post=bestpost):
        print(v.time_in)
        print(v.user.username)
        print(v.rating_comment)
        print(v.text)

