.. default-role:: code


处理大量数据
============

.. hint::

    阅读本章之前，请先确认你已经熟悉下列概念：

        函数 输入 输出 列表 布尔值

    如果有任何疑问，请重新阅读前面的章节。


引子：生成大量数据
------------------

编写程序很多时候都是因为要处理大量的数据。毕竟，计算机程序的一大优势就是既快速又不知疲倦，非常适合用于执行比如从大量样本中找出符合条件的数据，发送许多封内容相同只有收件人不同的邮件，批量转换图片、音乐或视频的格式，等等诸如此类的任务。本章我们讨论编程解决这类涉及大量数据的问题的基本方法。

在开始学习如何处理大量数据之前，我们必须先有大量数据用来处理才行。迄今为止，我们所有例题和习题中的数据，基本都是直接在程序中写出来的，因此数量都不算多。唯一的例外是涉及“文件夹中所有文件”的情况，我们用 `list_all_files()` 函数可以得到包含大量元素的列表。这本质上是在使用事先准备好的数据（很可能是别人而非我们自己准备的）。

除了文件的路径，我们也可以用文件本身包含的内容作为事先转备好的数据。请看下面的代码：

    ::

        from fileutils import read_text

        path = 'abc.txt'
        text = read_text(path)

其中用到了一个从 `fileutils.py` 中引入的新函数 `read_text()` ，其参数是一个表示文件路径的字符串，返回值是该路径所指向的文件的内容。假如文件 `abc.txt` 的内容是一行文字 `Hello, world!` ，那么 `text` 所代表的就是字符串 `'Hello, world!\n'` 。

文件可以包含长达很多行的文字内容。例如 `fileutils.py` 这个文件，其中包含超过100行Python代码。我们可以用 `read_text()` 来读出这些内容：

    ::

        path = 'fileutils.py'
        code = read_text(path)
        lines = code.splitlines()

这次我们不仅读出了 `fileutils.py` 中的内容（用名字 `code` 代表），还使用了另一个新函数 `splitlines()` 将 `code` 所代表的字符串变成了一个列表 `lines` ， `code` 中的每一行代码内容， 都会变成 `lines` 中的一个元素。字符串或是代表字符串的名字，都可以用 `splitlines()` 把自己包含的多行文字，变为一行行文字组成的列表。

再进一步，对于 `lines` 中的某个元素，也就是一行代码，我们可以用另一个新函数 `split()` 将其变为由单词组成的列表：

    ::

        line = lines[2]  # eg: 'from os import path'
        words = line.split()

与 `splitlines()` 相似，字符串或是代表字符串的名字，都可以用 `split()` 把自己变成由空格分隔开的单词的列表。

我们顺便再介绍一个与 `read_text()` 对应的函数 `write_text()` ，同样是来自 `fileutils.py` ：

    ::

        from fileutils import write_text

        path = 'abc.txt'
        text = 'Hello, world!\n'
        write_text(path, text)

如你所见， `write_text()` 函数的输入是两个字符串 `path` 和 `text` ，分别代表文件路径和一段文字内容。函数的效果是将文字内容 `text` 写入到路径 `path` 所指向的文件。因此这段代码执行后，我们就会得到一个路径为 `abc.txt` ，内容为一行文字 `Hello, world!` 的文件。你应该也注意到，我们没有用一个名字来代表 `write_text()` 的返回值，因为这个函数的返回值为 `None` ，或者说没有返回值。

本章接下来的各个小节会讲解如何用这些函数来写出处理大量数据的有用程序。更后面的章节会讲解如何实现类似 `split()` 和 `splitlines()` 这样的，将原本是一个整体的数据拆分为多个数据从而构造列表的函数。


映射和过滤
----------

在某些情况下，我们可能会需要设计这样的函数：输入是一批数据（当然，是放在某种容器中），输出也是一批数据，输入和输出的数据之间是一一对应的。这就叫做 *映射（map）* 。

    +-------------------------------+
    |     *f(x)* = *x*:sup:`2`      |
    +--------+---+----+---+----+----+
    |   *x*  | 2 |  5 | 3 |  4 |  7 |
    +--------+---+----+---+----+----+
    | *f(x)* | 4 | 25 | 9 | 16 | 49 |
    +--------+---+----+---+----+----+

在上面的表格中，我们通过函数 *f(x)* = *x*:sup:`2` ，分别作用于5个数值，从而得到另外5个数值。如果我们将之前的5个数值看做一个列表A，得到的5个数值看成另一个列表B，就可以说：

    列表B是列表A通过函数 *f(x)* = *x*:sup:`2` 得到的映射。

映射可以将一个列表中的数值全部转换为另一种形式，从而得到一个新的列表。巧妙利用这一点可以解决相当一部分问题。

还记得之前有一道练习题要求计算文件夹中文件的总大小吗？我们希望你当时已经成功写出了主程序：

    ::

        def main():
            dir_path = r'C:\Windows\System32'
            all_files = list_all_files(dir_path)
            file_sizes = list_file_sizes(all_files)
            size = sum(file_sizes)
            print(size)

由于 ``sum()`` 函数并不像 ``max()`` 一样支持 ``key`` 参数，我们不能直接把文件路径的列表传给 ``max()`` 。因此需要先用 ``list_file_sizes()`` 函数，把 **文件路径的列表** 转换成 **文件大小的列表** 。这就是一个典型的映射。

现在我们来学习如何实现 ``list_file_sizes()`` 函数。如前所述， ``list_file_sizes()`` 函数的输入是文件路径的列表，输出是文件大小的列表。我们据此写出函数框架：

    ::

        def list_file_sizes(paths):
            sizes = ... paths ...
            return sizes

剩下的工作就是由文件路径的列表得到文件大小的列表。显然，我们首先要能由单个文件路径得到对应的文件大小：

    ::

            size = get_file_size(path)

既然单个的 ``size`` 能够通过 ``get_file_size(path)`` 得到，那么要得到文件大小的列表 ``sizes`` ，我们就可以对列表 ``paths`` 中的每个文件路径 ``path`` 执行 ``get_file_size(path)`` 。把这个思路写成英语的话大致是这样：

    ::

            sizes = get_file_size(path) for each path in paths

虽然这并不是可以直接执行的代码，但与Python规定的正确表达方式也相去不远：

    ::

            sizes = [get_file_size(path) for path in paths]

我们从这行代码中可以还原出以下信息：

    1. ``sizes`` 是一个列表（注意 ``[]`` ）
    2. ``sizes`` 中的每个元素与 ``paths`` 中的每个元素一一对应（ ``... in paths`` ）
    3. 对应的方法是：``paths`` 中的 ``path`` 对应到 ``sizes`` 中就变成 ``get_file_size(path)``

这就是映射的3个要素：映射的数据类型，映射的数据来源，以及映射的数据转换方法。

由于这个从文件路径列表到文件大小列表的映射只需要一行代码，你可能会想把这个映射直接放进主程序。不过我们仍然推荐你把它放在单独的函数中：

    ::

        def list_file_sizes(paths):
            sizes = [get_file_size(path) for path in paths]
            return sizes

.. sidebar:: 说明

    把实现细节放在单独的函数中是一个好习惯。这一方面保持了主程序的表达简明，一方面也为之后改进函数留了余地。

列表映射的一般形式如下：

    ::

            c2 = [f(x) for x in c1]

其中 ``c1`` 和 ``c2`` 分别是映射前和映射后的列表， ``x`` 是 ``c1`` 中的元素， ``f(x)`` 是映射到 ``c2`` 中的元素，而 ``f()`` 就是对每个元素执行转换的函数。

掌握映射的关键，除了牢记语法，就在于确定 ``f()`` 了。诀窍与之前一样，首先明确 ``f()`` 的输入（映射前的元素）和输出（映射后的元素）作为提示。

.. topic:: Exercise

    写出下列映射：

        1. 一组文件中每个文件的修改时间
        2. 一组字符串中每个字符串的长度
        3. 一组字符串中每个字符串的首字母
        4. 一个数列中每个数的2倍
        5. 一个数列中每个数的平方
        6. 一个数列中每个数的倒数
        7. 一组动物中每种动物的腿的条数
        8. 一组学生成绩（0-100的数值）中每个学生是否及格（>=60）

现在来处理稍微复杂一些的情况。例如我们不需要列出全部文件的大小，而是只需要图片文件的大小。此时输出中的数据只对应输入中的部分数据而非全部。这就叫做 *过滤（filter）* 。

    ::

            image_sizes = [get_file_size(path) for path in paths if is_image(path)]

对照一下原先的全部文件大小的映射，就只有在最后多了一个 ``if is_image(path)`` 。这个 ``is_image()`` 函数称作 *过滤条件* ，或者叫做 *谓词* 。该函数对输入列表中的每个元素返回一个布尔值，输出的列表中只会包含过滤条件返回为 ``True`` 的那些元素。

我们可以把上面的代码拆解成如下两行代码：

    ::

            image_paths = [path for path in paths if is_image(path)]
            image_sizes = [get_file_size(path) for path in image_paths]

第一行代码是从所有路径的列表中过滤出只包含图片文件的列表，第二行代码就只做了普通的映射，将图片文件路径的列表映射为图片文件大小的列表。

如果过滤条件只是进行简单比较（诸如 ``==`` ``!=`` ``>`` 之类），我们也可以直接写在 ``if`` 后面。例如：

    ::

            work_days = [day for day in days if day != 'Sunday']
            small_nums = [num for num in nums if num < 100]

带有过滤条件的列表映射的一般形式如下：

    ::

            c2 = [f(x) for x in c1 if p(x)]

其中 ``p()`` 就是过滤条件。

    +---------------------------------------------+
    |    *f(x)* = *x*:sup:`2` , *p(x)* = x > 3    |
    +--------+-------+------+-------+------+------+
    |   *x*  |   2   |   5  |   3   |   4  |   7  |
    +--------+-------+------+-------+------+------+
    | *p(x)* | False | True | False | True | True |
    +--------+-------+------+-------+------+------+
    | *f(x)* |       |  25  |       |  16  |  49  |
    +--------+-------+------+-------+------+------+

在上面的表格中，我们通过函数 *p(x)* = x > 3 ，分别作用于5个数值，从中选出了3个数值。再通过函数 *f(x)* = *x*:sup:`2` ，分别作用于选出的3个数值，从而得到另外3个数值。这是一个带过滤条件的映射的例子。

.. topic:: Exercise

    写出下列带有过滤条件的映射：

        1. 一组路径（文件或文件夹）中每个文件的修改时间
        2. 一组字符串中首字母为a的字符串的长度
        3. 一个数列中每个大于1的数的倒数
        4. 一个数列中每个奇数的平方
        5. 一组动物中2条腿的动物
        6. 一组学生成绩（0-100的数值）中及格（>=60）的学生成绩


广义映射
--------

我们已经知道映射是对列表中的每个元素 `x` 都应用同一个函数 `f(x)` ，得到另一个列表。

    ::

        nums = [1, 2, 3, 4, 5]
        quads = [x * x for x in nums]

上例中的列表 `nums` 通过平方运算得到了新列表 `quads` ，内容是 `[1, 4, 9, 16, 25]` 。

我们也知道，除了这种既有输入又有输出的函数，还有很多只有输入没有输出的函数（例如 `print()` ），甚至还有既无输入也无输出的函数（例如 `sleep()` ）。这些没有输出的函数，其有用性不在于通过某种运算或转换得到新数据，而在于得到与数据有关或无关的某种 **效果** 。如果我们使用这些函数来构造映射，也就是说，对列表中的每个元素应用这些函数，就能够得到与元素数量相同的一批 **效果** 。

例如我们可以对列表中的每个元素应用 `print()` 函数：

    ::

        lines = [
            'Beautiful is better than ugly',
            'Explicit is better than implicit',
            'Simple is better than complex',
        ]
        prints = [print(x) for x in lines]

还记得吗？ `print()` 函数的返回值永远是 `None` ，也就是说我们得到的新列表 `prints` 的内容是 `[None, None, None]` ，并不是什么有意义的数据。但我们也并非一无所获，在得到这个新列表的同时，屏幕上还显示出了3行文字。也就是说，这个映射可以帮助我们将列表中包含的多个字符串都显示在屏幕上。

在这个例子中，对我们有用的是映射过程中 **顺便** 在屏幕上显示出的文字，而非映射得到的列表，因此我们也不需要 `prints` 这个名字来表示任何数据。

    ::

        [print(x) for x in lines]

由于等号和等号左边的名字都不存在，这个映射得到的列表就相当于被马上抛弃了。对于这种只需要映射过程中带来的效果，而不需要映射得到的新数据的情况，我们通常使用下面的写法：

    ::

        for x in lines:
            print(x)

这种新的写法叫做 *for代码块* 。在这种写法中，元素全为 `None` 的无用列表，即使在形式上也不存在了。但请注意这仍然是一个映射。

我们再来看下面的代码片段，其中用到了另一个返回值为 `None` 的函数 `list.extend()` ：

    ::

        small_lists = [[1, 2, 3], [4, 5, 6, 7], [8, 9]]
        big_list = []
        for small_list in small_lists:
            big_list.extend(small_list)

这段代码会让 `big_list` 从空列表变为一个包含3个小列表中所有元素的大列表 `[1, 2, 3, 4, 5, 6, 7, 8, 9]` 。这同样是利用映射过程中带来的效果做到的。

下面这段代码展示了可以在for代码块内部包含多行代码：

    ::

        students = [
            {'name': 'Alice', 'score': 90},
            {'name': 'Bob', 'score': 100},
            {'name': 'Carol', 'score': 92},
            {'name': 'David', 'score': 55},
            {'name': 'Emily', 'score': 62},
        ]
        for student in students:
            passed = student['score'] >= 60
            student['passed'] = passed

代码的最后3行相当于：

    ::

        def add_passed(student):
            passed = student['score'] >= 60
            student['passed'] = passed

        [add_passed(student) for student in students]

也就是相当于直接将函数 `add_passed()` 的代码（而非名字）放进了映射。函数 `add_passed()` 同样没有返回值，其效果是为字典 `student` 增加一对key和value，或者说增加一个字段 `passed` ，用于表示该学生的成绩是否及格。因此这个映射（无论两个版本中的哪一个）将为列表中的每个字典都增加 `passed` 字段。也就是说列表 `students` 中的内容会变成：

    ::

        students = [
            {'name': 'Alice', 'score': 90, 'passed': True},
            {'name': 'Bob', 'score': 100, 'passed': True},
            {'name': 'Carol', 'score': 92, 'passed': True},
            {'name': 'David', 'score': 55, 'passed': False},
            {'name': 'Emily', 'score': 62, 'passed': True},
        ]

在本章开头介绍过的 `write_text()` 也是一个没有返回值的函数。我们在for代码块中使用 `write_text()` 函数：

    ::

        from fileutils import write_text

        names = ['Alice', 'Bob', 'Carol', 'David', 'Emily']

        for name in names:
            path = '{}.txt'.format(name)
            text = 'Hello, {}!'.format(name)
            write_text(path, text)

同样的，for代码块中的内容相当于下面的函数和映射：

    ::

        def write_letter(name):
            path = '{}.txt'.format(name)
            text = 'Hello, {}!'.format(name)
            write_text(path, text)

        [write_letter(name) for name in names]

在两个版本的代码中，列表 `names` 中的每个 `name` 最终都映射到一个 `write_text()` 操作，而 `write_text()` 的参数 `path` 和 `text` ，则都是由 `name` 构造出的字符串。最终的结果是，我们从列表中的5个名字，得到了5个路径和内容各不相同的文件。

.. topic:: Exercise

    运行上面两个版本的关于 `write_text()` 的代码，比较两个版本的运行效果是否相同。

在上面这些例子中，我们利用能够得到某种效果的函数，从列表中的一批数据得到了一批效果。这与利用对数据进行运算或转换的函数，从列表中的一批数据得到另一批数据，在构造上是完全相同的。因此我们可以将以上这些例子中的代码称为 *广义映射* 。在程序设计的回溯环节，如果我们需要从一批数据得到另一批数据，就可以考虑运用映射；如果我们需要从一批数据得到一批效果，或是利用这批效果来构造新的数据，就可以考虑运用广义映射。

.. topic:: Exercise

    用for代码块的形式写出下列映射：

        1. 在屏幕上显示出某个字典中所有的value
        2. 同上，但是每显示一个value就休息1秒钟再打印下一个value


实例：成绩通知单
--------------------

经过前面各节的铺垫，现在时机已经成熟。我们可以运用已经学到的各种方法，来完成一个能处理实际问题的完整程序。

.. topic:: 实例：成绩通知单

    假设我们有类似下表的一组学生成绩。

        +-------+-----------------+
        | Name  |      Scores     |
        |       +-----+-----+-----+
        |       |  A  |  B  |  C  |
        +=======+=====+=====+=====+
        | Alice |  85 |  90 |  77 |
        +-------+-----+-----+-----+
        | Bob   |  95 | 100 |  98 |
        +-------+-----+-----+-----+
        | Carol |  80 |  92 |  69 |
        +-------+-----+-----+-----+
        | David |  90 |  55 |  90 |
        +-------+-----+-----+-----+
        | Emily |  61 |  62 |  60 |
        +-------+-----+-----+-----+

    编写程序为每位学生生成成绩通知单并存到文件。通知单的内容应包括学生名字、各科平均分以及是否及格。及格的判断标准是没有任何一科低于60分。

题目的表格中虽然只列出了5条数据，但真正的成绩表肯定远远不只这么多。为了处理大量的学生成绩，我们将使用映射来处理这批数据。

    1. 明确输入输出

        输入是存有学生成绩表的文件路径，输出是对应的成绩通知单。

    2. 确定输入输出数据的格式

        * 输入 `input_path` 是表示成绩表文件路径的字符串，比如 `'students.txt'`
        * 输出是 **若干** 写入文件的成绩通知单，对于每份成绩通知单，我们用 `write_text(output_path, transcripts)` 执行文件写入。其中：

            - `output_path` 是表示成绩通知单的写入路径的字符串，比如 `'Alice.txt'`
            - `transcripts` 是表示成绩通知单的内容的字符串，比如 `'Dear Alice, ...'`

    3. 从输出数据开始回溯

        如前所述，由于我们要写入多个文件，这里需要 `for ... in ...` 来构造映射。

        ::

            def main():
                input_path = 'students.txt'
                ...
                for ... in ... :
                    write_text(output_path, transcript)

        由于每个 `write_text()` 操作都需要一组 `output_path` 和 `transcript` ，映射的来源就应该是一个包含若干组 `output_path` 和 `transcript` 的列表。我们将这个列表命名为 `transcripts` ：

        ::

            def main():
                input_path = 'students.txt'
                ...
                for output_path, transcript in transcripts:
                    write_text(output_path, transcript)

    4. 继续回溯直到输入数据

        现在我们需要将列表 `transcripts` 表示成由另一个列表映射而来。显然， `transcripts` 中所包含的两类数据， `output_path` 和 `transcript` 都是由学生成绩表中的数据得来。我们不妨假设一个存有学生成绩表中所有数据的列表，将其命名为 `score_table` ：

        ::

            def main():
                input_path = 'students.txt'
                ...
                transcripts = make_transcript(row) for row in score_table
                for output_path, transcript in transcripts:
                    write_text(output_path, transcript)

        如上所示， `transcripts` 中的每一组 `output_path` 和 `transcript` 都是由 `score_table` 中的一行数据 `row` 经函数 `make_transcript()` 映射而来。

        接下来，我们用一个函数 `read_score_table()`  从文件中读取出学生成绩表：

        ::

            def main():
                input_path = 'students.txt'
                score_table = read_score_table(input_path)
                transcripts = make_transcript(row) for row in score_table
                for output_path, transcript in transcripts:
                    write_text(output_path, transcript)

        至此我们顺利完成回溯。

    5. 整理所需函数

        在回溯过程中我们引入了两个函数 `read_score_table()` 和 `make_transcript()` 。这两个函数都是特定于题目要求的，无论Python标准库还是第三方库都并不存在这样的函数，因此必须由我们自行实现。

    6. 实现所需函数

        需要实现的两个函数 `read_score_table()` 和 `make_transcript()` ，其中 `read_score_table()` 与前面的例题大同小异，我们留做练习题； `make_transcript()` 函数下面会展开讲解。

接下来我们来实现 `make_transcript()` 函数。

    1. 明确输入输出

        * 输入是学生成绩表中的一行数据，包含学生姓名和各科成绩
        * 输出是成绩通知书的文件路径和内容

    2. 确定输入输出数据的格式

        * 输入数据 `row` 我们可以采用字典，包含 `name` 和 `scores` 两个字段。其中：

            - `name` 是表示学生姓名的字符串，比如 `'Alice'`
            - `score` 是存储各科成绩的列表，其中包含若干个数值，比如 `[85, 90, 77]`

        * 输出数据包含2项，格式和含义都已经由调用方事先确定了，这里再列出一次：

            - `output_path` 是表示成绩通知单的写入路径的字符串，比如 `'Alice.txt'`
            - `transcripts` 是表示成绩通知单的内容的字符串，比如 `'Dear Alice, ...'`

        由此得到函数的模板如下：

        ::

            def make_transcript(row):
                ...
                return output_path, transcript

    3. 从输出数据开始回溯

        两项输出数据中的 `output_path` ，我们简单地使用学生名字 `name` 加上 `'.txt'` 作为成绩通知单的文件名即可。而成绩通知单的内容 `transcript` ，根据题目要求，需要包含学生名字 `name` 、各科平均分 `avg_score` 、是否及格 `is_passed` 这3项信息。我们可以把这些信息放进一个字符串模板。写出代码如下：

        ::

            def make_transcript(row):
                ...
                tmpl = '''
                    Dear {}:
                        Your average score is {}.
                        You have {} the exam.
                '''
                transcript = tmpl.format(name, avg_score, is_passed)
                output_path = '{}.txt'.format(name)
                return output_path, transcript

    4. 继续回溯直到输入数据

        接下来的问题就是设法表示出这3项信息。先看各科平均分：

        ::

            avg_score = sum(scores) / len(scores)

        这里 `scores` 是包含该名学生所有科目成绩的列表。

        判断是否及格也很简单，只要判断 `scores` 中的各个数值 **全部** 在60以上：

        ::

            if all(score >= 60 for score in scores):
                is_passed = 'passed'
            else:
                is_passed = 'not passed'

        而学生名字 `name` 和各科成绩 `scores` ，都已经包含在了输入数据 `row` 之中。

        ::

            name = row['name']
            scores = row['scores']

        将上面讨论过的代码行放进程序，得到：

        ::

            def make_transcript(row):
                name = row['name']
                scores = row['scores']
                avg_score = sum(scores) / len(scores)
                is_passed = all(score >= 60 for score in scores)
                tmpl = '''
                Dear {}:
                    Your average score is {}.
                    You have {} the exam.
                '''
                transcript = tmpl.format(name, avg_score, is_passed)
                output_path = '{}.txt'.format(name)
                return output_path, transcript

        到这里我们就完成了回溯。

    5. 整理所需函数

        在回溯过程中没有引入任何新的函数。

    6. 实现所需函数

        没有需要实现的函数
