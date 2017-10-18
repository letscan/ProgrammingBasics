对数据分组
==========

.. hint::

    阅读本章之前，请先确认你已经熟悉下列概念： ::

        映射 过滤 列表 字典

    如果有任何疑问，请重新阅读前面的章节。


分组的原理
----------

有道是“物以类聚，人以群分”。把一大堆东西按各种标准分成不同的组，可说是（强迫症）人类的天性之一。生物学家把生物分成界门纲目科属种，图书馆把书分成几十个大类和几百的小类依次排上书架，聊天软件允许你把好友放进不同分组。这些都是人类爱好分组的例子。

.. sidebar:: 说明

    值的注意的是，无论是上面举出的例子，还是你能想到的其它分组的例子，对于分组的标准，人们总是存在争议。

但凡分组，必然涉及到两个要素：一是需要分组的一大堆东西，二是对它们进行分组的标准。

例如我们手头有一副乱序的扑克牌，若要将它们整理好，你会怎么做？

不同的人有不同的选择。有人会按照花色将牌分为4组，每组13张。也有人会按点数将牌分为13组，每组4张。

无论采用哪种标准，整理扑克的过程大致都是一样：对每一张牌，通过观察确定它归属哪个分组，然后把它加入相应分组的牌堆。

对一批对象中的每一个都进行操作，这与我们已经学过的映射非常相似。

    .. code-block:: python

        ... add_to_group(card) for card in cards ...

如果要用一种数据类型表示整理好的扑克，字典是个不错的选择。如果按花色分组的话，我们可以用花色作为key，各组牌堆作为value，分别用一个列表表示。按点数分组的情况也是类似。

    .. code-block:: python

        card_groups = {
            '♠': ['A', 'K', 'Q', ...]
            '♥': ['A', 'K', 'Q', ...]
            '♣': ['A', 'K', 'Q', ...]
            '♦': ['A', 'K', 'Q', ...]
        }

本章我们就介绍如何利用映射和字典来编程解决各种分组问题。


分组统计
--------

对事物进行分组的常用目的之一，就是对各个分组进行统计。例如统计每个分组包含的物品的数量，或是对每个分组中物品的某个指标进行求和（总重量、总价格等），然后还可以在各个分组之间对统计结果进行比较。我们来看一个例子：

.. topic:: 拍照最多的一天

    假设我们把拍摄的照片都存放在一个文件夹中，这些照片各自拍摄于不同的日期，如果能够统计出哪些日期拍摄的照片最多，就可以知道我们在那些日期参加了重要的活动。

    将指定文件夹中所有的照片按拍摄日期（精确到天）分组，找出拍摄照片张数最多的一天。

先来简单分析一下这个问题。与之前的问题不同的是，我们要处理的不是文件夹中的所有文件，而是只处理图片文件， ``list_all_files()`` 并不完全适用。另外由于要求是按天来分组，我们需要得到精确到天的日期，只靠 ``getmtime()`` 也是不行的。

明确这些前提之后，我们可以开始按照编程方法一步步进行了：

    1. 明确输入和输出

        输入是一个文件夹路径，输出是一个日期

    2. 确定数据类型

        * 输入的文件夹路径 ``dir_path`` 类型为 ``str`` ，例如： ``'C:\\My Photos'``
        * 输出的日期 ``big_day`` 类型为 ``date``，例如： ``date(2017, 10, 1)``

    3. 从输出开始回溯

        .. code-block:: python

                big_day = max(photo_by_date, key=len)
                print('Most photo date: ', big_day)

        这里的 ``photo_by_date`` 是一个字典，key是日期，value是照片列表。

    4. 继续回溯直到输入数据

        .. code-block:: python

                dir_path = 'C:\\My Photos'
                photos = list_all_photos(dir_path)
                photo_by_date = group_photo_by_date(photos)
                big_day = find_big_day(photo_by_date)
                print('Most photo date: ', big_day)

        其中 ``photos`` 是一个文件路径的列表，且只包含照片文件。而 ``dir_path`` 已经是输入数据。回溯完毕。

    5. 整理所需函数

        整个过程中引入了3个函数： ``list_all_photos()`` 、 ``group_photo_by_date()`` 和 ``find_big_day()`` 。

        这3个函数都没法通过引用来解决，全部需要我们来实现。

    6. 实现所需函数

        虽然需要实现的函数有3个，但 ``list_all_photos()`` 可以由 ``list_all_files()`` 加上过滤得到，``find_big_day()`` 也只是 ``max()`` 的又一次应用。这两个函数留作习题请你来实现。

        我们现在进入正题，实现 ``group_photo_by_date()`` 这个分组函数。先写出函数框架：

            .. code-block:: python

                def group_photo_by_date(photos):
                    groups = ... photos ...
                    return groups

        如前所述， ``photos`` 是文件路径的列表， ``groups`` 是一个key为日期、value为照片列表的字典。要得到这样一个字典需要一点技巧。

        我们先假设已经有如下的字典：

            .. code-block:: python

                groups = {
                    date(2017, 1, 1): [],
                    date(2017, 1, 2): [],
                    date(2017, 1, 3): [],
                    ... ...
                    date(2017, 12, 31): [],
                }

        再假设某张照片a.jpg的拍摄日期是2017年1月1日，另一张照片b.jpg的拍摄日期是2017年1月2日，我们可以这样把两张照片加入 ``groups`` ：

            .. code-block:: python

                groups[date(2017, 1, 1)].append('a.jpg')
                groups[date(2017, 1, 2)].append('b.jpg')

        我们通过 ``groups[date(2017, 1, 1)]`` 和 ``groups[date(2017, 1, 2)]`` 分别取到两个日期对应的空列表 ``[]`` ，然后通过 ``append()`` 分别向两个空列表中各添加了一个元素。

        此时字典的内容变成如下所示：

            .. code-block:: python

                groups = {
                    date(2017, 1, 1): ['a.jpg'],
                    date(2017, 1, 2): ['b.jpg'],
                    date(2017, 1, 3): [],
                    ... ...
                    date(2017, 12, 31): [],
                }

        假设第3张照片c.jpg的拍摄日期也是2017年1月1日，用同样的方法将其加入 ``groups`` ：

            .. code-block:: python

                groups[date(2017, 1, 1)].append('c.jpg')

        这次 ``groups[date(2017, 1, 1)]`` 取到的已经不是空列表 ``[]`` 而是 ``['a.jpg']`` ，再次通过 ``append()`` 向其中添加一个元素后，整个字典的内容变成如下所示：

            .. code-block:: python

                groups = {
                    date(2017, 1, 1): ['a.jpg', 'c.jpg'],
                    date(2017, 1, 2): ['b.jpg'],
                    date(2017, 1, 3): [],
                    ... ...
                    date(2017, 12, 31): [],
                }

        推而广之，对每张照片 ``photo`` 我们都可以用其拍摄日期作为key，将其添加到 ``groups`` 中相应的列表。假设我们已经有这个获取照片拍摄日期的函数 ``get_photo_date(photo)`` ，将任一 ``photo`` 添加到适当列表的代码可以这样写：

            .. code-block:: python

                groups[get_photo_date(photo)].append(photo)

        结合前面已经学到的映射，我们就可以将列表 ``photos`` 中的所有元素添加到到字典 ``groups`` 中：

            .. code-block:: python

                ... = [groups[get_photo_date(photo)].append(photo) for photo in photos]

        等等！这里似乎出现了问题。等号左边应该写什么呢？如果你还记得 ``append()`` 的返回值总是 ``None`` ，就可以预测这个映射得到的只是一个全部由 ``None`` 组成的列表，我们需要的并非这个列表而是字典 ``groups`` 。

        当然我们也可以直接省略等号及等号左边，也就是放弃映射的结果，而只是利用这个过程的“副作用”：向 ``groups`` 中的各个列表添加元素。

            .. code-block:: python

                def group_photo_by_date(photos):
                    [groups[get_photo_date(photo)].append(photo) for photo in photos]
                    return groups

        但通常我们还是推荐另一种更清晰的写法：

            .. code-block:: python

                def group_photo_by_date(photos):
                    for photo in photos:
                        key = get_photo_date(photo)
                        groups[key].append(photo)
                    return groups

        .. note::

            这种新的写法叫做 *for语句块* ，适合不需要映射结果、只需要映射过程的“副作用”的场景。同时，for语句块内部允许包含多行代码，利用得当的话可以使代码更清晰易读。我们以后会详细讨论for语句块的各种用法。

        我们还是将注意力转回 ``groups`` 。注意现在 ``group`` 这个名字还没有被定义！包含所有日期作为key的字典是我们假设出来的，实际上并不存在这样一个字典（想想怎么可能包含 **所有的** 日期）。一旦某张照片的拍摄日期不在 ``groups`` 所包含的key的范围之内，就会引发异常 ``KeyError`` 。

        好在Python提供了一个工具帮我们解决这个问题：

            .. code-block:: python

                from collections import defaultdict

                def group_photo_by_date(photos):
                    groups = defaultdict(list)
                    ...

        这里 ``defaultdict(list)`` 会返回一个特殊的字典：如果你指定的key还不存在，就返回一个 ``list`` 也就是 ``[]`` 作为value，而不会引发 ``KeyError`` 。这样我们就不必操心如何在 ``groups`` 中事先准备好大量的日期作为key。

        现在我们终于可以写出完整的 ``group_photo_by_date()`` 函数了：

            .. code-block:: python

                from collections import defaultdict

                def group_photo_by_date(photos):
                    groups = defaultdict(list)
                    for photo in photos:
                        key = get_photo_date(photo)
                        groups[key].append(photo)
                    return groups

        其中 ``get_photo_date()`` 是新增的需要实现的函数。这个函数也作为习题留给你来实现。

.. topic:: Exercise

    实现 ``list_all_photos()`` ，``get_photo_date()`` 和 ``find_big_day()`` ，使照片分组程序可以完整执行。

.. topic:: Exercise

    用for语句块的形式写出下列映射：

        1. 在屏幕上打印出某个字典中所有的value
        2. 同上，但是每打印一个value就暂停1秒钟再打印下一个value

回顾一下写好的程序：

    .. code-block:: python

        # coding: utf-8
        """目标：找出指定文件夹中的重复文件
        """
        from collections import defaultdict

        from fileutils import list_all_files, get_file_sha1

        ...

        def find_big_day(photo_by_date):
            big_day = ... photo_by_date ...
            return big_day

        def group_photo_by_date(photos):
            groups = defaultdict(list)
            for photo in photos:
                key = get_photo_date(photo)
                groups[key].append(photo)
            return groups

        def main():
            dir_path = 'C:\\My Photos'
            photos = list_all_photos(dir_path)
            photo_by_date = group_photo_by_date(photos)
            big_day = find_big_day(photo_by_date)
            print('Most photo date: ', big_day)

        if __name__ == '__main__':
            main()

顾名思义，分组统计的程序至少需要有 **分组** 和 **统计** 两个核心步骤。在上面的程序中， ``group_photo_by_date()`` 是分组函数， ``find_big_day()`` 是统计函数。统计函数会在内部借助 ``sum()`` 、 ``len()`` 、 ``max()`` 或其它类似的函数来实现功能，我们已经非常熟悉了。分组函数的实现方法是本章关注的重点。


实例：找出重复文件
--------------------

作为巩固，我们来看另一个用到分组的例子。

.. topic:: 找出重复文件

    我们的电脑中的文件，可能会有很多是互相重复的，也就是说：2个或者2个以上的文件，内容完全相同。编写程序找出指定文件夹下的所有重复文件，将它们分组列出。

解决这个问题需要将文件按内容进行分组，每个分组中的文件，内容都完全一样。与前例不同的是，我们最后要得到的不是每个分组的数量，而是分组中具体的文件路径。除此之外，解题过程与前面的例子完全类似：

    1. 明确输入和输出

        输入是一个文件夹路径，输出是一个列表，列表中的每一项是一组互相重复的文件

    2. 确定数据类型

        * 输入的文件夹路径 ``dir_path`` 类型为 ``str`` ，例如： ``'C:\\Windows\\System32'``
        * 输出的日期 ``dup_files`` 类型为嵌套 ``list``，例如： ``[['a1', 'a2'], ['b1', 'b2', 'b3']]``

    3. 从输出开始回溯

        观察 ``dup_files`` 的格式，结合前面的例题，这强烈提示我们用一个分组函数来得到 ``dup_files`` 。

        .. code-block:: python

                dup_files = group_file_by_content(all_files)
                print('dup_files: ', dup_files)

    4. 继续回溯直到输入数据

        我们已经非常熟悉 ``all_files`` 了。照例请出老朋友 ``list_all_files()`` 。

        .. code-block:: python

                dir_path = 'C:\\Windows\\System32'
                all_files = list_all_files(dir_path)
                dup_files = group_file_by_content(all_files)
                print('dup_files: ', dup_files)

        这次的回溯非常轻松。

    5. 整理所需函数

        需要的函数有2个：老朋友 ``list_all_files()`` 可以直接 ``import`` ， ``group_file_by_content()`` 我们马上就来实现。

    6. 实现所需函数

        同样是分组函数，实现 ``group_file_by_content()`` 的过程完全可以参照 ``group_photo_by_date()`` 。我们直接写出一个相对完整的函数框架：

            .. code-block:: python

                def group_file_by_content(paths):
                    groups = defaultdict(list)
                    for path in paths:
                        key = ... path ...
                        groups[key].append(path)
                    return groups

        唯一的问题就是用什么作为每个文件的key。直接用整个文件的内容作为key虽然简单粗暴但也未尝不可，不过我们还是推荐一个较为优雅的方案，也是所谓的业界惯例：取文件的 **sha1** 值。

            .. code-block:: python

                        key = get_file_sha1(path)

        我们在 :download:`fileutils.py <../fileutils.py>` 中提供了 ``get_file_sha1()`` 函数，直接引用即可。

        完整的 ``group_file_by_content()`` 函数实现如下：

            .. code-block:: python

                from fileutils import get_file_sha1

                def group_file_by_content(paths):
                    groups = defaultdict(list)
                    for path in paths:
                        key = get_file_sha1(path)
                        groups[key].append(path)
                    return groups

回顾下我们的重复文件查找程序的完整代码：

    .. code-block:: python

        # coding: utf-8
        """目标：找出指定文件夹中的重复文件
        """
        from collections import defaultdict

        from fileutils import list_all_files, get_file_sha1


        def group_file_by_content(paths):
            groups = defaultdict(list)
            for path in paths:
                key = get_file_sha1(path)
                groups[key].append(path)
            return groups

        def main():
            dir_path = 'C:\\Windows\\System32'
            all_files = list_all_files(dir_path)
            dup_files = group_file_by_content(all_files)
            print('dup_files: ', dup_files)

        if __name__ == '__main__':
            main()

这个程序应该是可以成功运行的，但有一个小问题：你会发现最后的 ``print()`` 输出的内容实在太长，而且在屏幕上挤作一团，实际上根本没法看。这里我们通过一道练习题先解决这个问题：

.. topic:: Exercise

    实现函数 ``print_list()`` 用于打印列表，每行只打印列表中的一个元素。

如果你成功实现了 ``print_list()`` 并用它代替 ``print()`` 来显示我们找到的各组重复文件，你也许就能发现这个问题：输出结果的内层列表中，有一些只包含一个文件。

由于每个内层列表的内容都是一组互相重复的文件，只包含一个文件的分组，按照定义来讲并不属于“重复文件”。严格来说，这是代码中的一个逻辑错误，也就是俗称的 *Bug* 。

既然发现了问题，我们就要修正这个Bug。好在这个问题并不难处理，只需要在 ``group_file_by_content()`` 的返回值与 ``dup_files`` 之间，增加一个过滤的环节：

    .. code-block:: python

            groups = group_file_by_content(all_files)
            dup_files = [group for group in groups if ... group ... ]

过滤条件也非常简单：只有包含2个或2个以上文件的分组，才属于重复文件。用代码表示就是 ``len(group) >= 2`` 。

    .. code-block:: python

            dup_files = [group for group in groups if len(group) >= 2]

为了保持程序清晰，我们还是将过滤的环节独立成一个函数：

    .. code-block:: python

        def find_dup_files(groups):
            dup_files = [group for group in groups if len(group) >= 2]
            return dup_files

修正后的重复文件查找程序的完整代码如下：

    .. code-block:: python

        # coding: utf-8
        """目标：找出指定文件夹中的重复文件
        """
        from collections import defaultdict

        from fileutils import list_all_files, get_file_sha1


        def group_file_by_content(paths):
            groups = defaultdict(list)
            for path in paths:
                key = get_file_sha1(path)
                groups[key].append(path)
            return groups

        def find_dup_files(groups):
            dup_files = [group for group in groups if len(group) >= 2]
            return dup_files

        def main():
            dir_path = 'C:\\Windows\\System32'
            all_files = list_all_files(dir_path)
            groups = group_file_by_content(all_files)
            dup_files = find_dup_files(groups)
            print('dup_files: ', dup_files)

        if __name__ == '__main__':
            main()

在这个例子中，我们在通常的程序设计完成之后，通过运行发现了问题，然后修正了问题。这种事后修正的情况在实际的程序设计过程中是经常发生的。有时是为了修正错误，有时只是为了改进程序。即使最有经验的程序员，也很难一次性就写出解决问题的完美程序。不断的优化与改进，也是学习程序设计中的重要一环。

.. topic:: Exercise

    请编程解决下列分组问题：

        1. 将一组字符串按首字母分组（不区分大小写）
        2. 将一组整数按个位数分组
        3. 将一组动物按腿的条数分组


通用的分组函数
--------------

观察我们在解决前面两道例题过程中创建的分组函数：

            .. code-block:: python

                def group_photo_by_date(photos):
                    groups = defaultdict(list)
                    for photo in photos:
                        key = get_photo_date(photo)
                        groups[key].append(photo)
                    return groups

            .. code-block:: python

                def group_file_by_content(paths):
                    groups = defaultdict(list)
                    for path in paths:
                        key = get_file_sha1(path)
                        groups[key].append(path)
                    return groups

不难发现，这两个函数除了一些名字上的差别，结构上是完全一致的！

由于名字只是一些代号，我们完全可以按需要更换掉现有的名字。现在我们把两个分组函数中用到的名字都换成意义更广泛的词语：

            .. code-block:: python

                def group_by(items):
                    groups = defaultdict(list)
                    for item in items:
                        key = get_photo_date(item)
                        groups[key].append(item)
                    return groups

            .. code-block:: python

                def group_by(items):
                    groups = defaultdict(list)
                    for item in items:
                        key = get_file_sha1(item)
                        groups[key].append(item)
                    return groups

现在两个分组函数的名字都改叫 ``group_by`` ，参数的名字和返回值的名字都完全一致，内部也只剩下一处差别: ``get_photo_date()`` 和 ``get_file_sha1()`` 这两个用于计算key的函数。我们把这两个函数也用同一个名字代表：

            .. code-block:: python

                def group_by(items):
                    get_key = get_photo_date

                    groups = defaultdict(list)
                    for item in items:
                        key = get_key(item)
                        groups[key].append(item)
                    return groups

            .. code-block:: python

                def group_by(items):
                    get_key = get_file_sha1

                    groups = defaultdict(list)
                    for item in items:
                        key = get_key(item)
                        groups[key].append(item)
                    return groups

现在只要把 ``get_key`` 移到 ``group_by()`` 的参数区域，就可以把这处唯一的不同也转移到函数外部：

            .. code-block:: python

                def group_by(items, get_key):
                    groups = defaultdict(list)
                    for item in items:
                        key = get_key(item)
                        groups[key].append(item)
                    return groups

原先调用 ``group_photo_by_date()`` 和调用 ``group_file_by_content()`` 的地方现在都可以调用 ``group_by()`` 来代替，只需要传递不同的参数：

            .. code-block:: python

                groups = group_by(all_photos, get_photo_date)


            .. code-block:: python

                groups = group_by(all_files, get_file_sha1)

以上将 ``group_photo_by_date()`` 和 ``group_file_by_content()`` 两个分组函数，统一成 ``group_by()`` 这个通用的分组函数的过程，又是一次 **消除重复** 的演练。

今后的程序设计中如果需要分组，可以直接使用 ``group_by()`` 函数。我们把这个函数的完整版本放在了附赠的 dictutils.py 中，你可以直接引用。

.. topic:: Exercise

    用 ``group_by()`` 重写前面的分组统计练习题


本章小结
--------

  * 解决分组统计问题的关键是设计分组函数和统计函数。

  * 设计分组函数的关键是用 ``defaultdict()`` 返回的特殊字典作为容器，再加上一个计算key的函数。

  * 程序的设计可能会有错误，错误需要被及时发现并改正。

  * 善于发现并消除程序中的重复代码，将个别不同的部分作为函数的参数。
