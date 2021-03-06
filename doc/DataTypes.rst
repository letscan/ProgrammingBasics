.. default-role:: code


Python常用数据类型
============================

.. hint::

    本章及后面的一些章节被冠名为 **间奏** 。这些章节的内容是Python特定的基础知识，相对而言是冗长而枯燥的。我们建议你快速浏览本章内容以获得一些印象，然后直接继续阅读后面的章节。等遇到问题时，再回到本章查找相关内容仔细阅读。


所谓数据类型
--------------------

迄今为止，我们已经见过了3种不同的 *数据类型* ：

  * 数值：比如 ``1`` ， ``2`` ， ``3.5`` 等
  * 字符串：比如 ``'Hello, world!\n'`` ， ``r'C:\Windows\System32'`` ， ``''`` 等
  * 列表：比如 ``['a', 'b', 'c', 'd', 'e']`` ， ``[1, 2, 3, 4, 5]`` ， ``[]`` 等

不难发现，3种数据类型都有各自明显的特征。数值由数字和小数点组成，字符串有一对 ``''`` 包围，列表则是有一对 ``[]`` 包围。

另一方面，列表与另外两种数据类型又有一个重要的区别：列表内部包含 ``,`` 分隔开的其它数据，可以是数值或字符串。我们通常把这种可以包含其它数据的数据类型称作 *容器* 。

除了外观，不同数据类型之间更重要的区别在于使用的场合。例如，我们可以对字符串和列表使用 ``len()`` 函数，但对数值却不行。相对的，``quad()`` 和 ``div_int()`` 函数的输入只能是数值，而不能是字符串或列表。

本章我们会介绍更多的数据类型，包括它们各自的外观特征，以及使用上的区别，尤其是几种非常有用的容器。正如我们已经知道的，编程的重要一步就是确定输入数据与输出数据的表示形式（也就是现在说的数据类型），已知函数的输入与输出（即数据类型间的转换关系）也是帮助思考操作步骤的重要线索。熟悉各种数据类型是掌握编程技能的重要基础。


“简单”数据类型
--------------------

说到 **简单** 的数据类型，在前面提到的3种数据类型之中，恐怕就要算 *数值* 数据类型了。但其实你已经 **见过** 了更简单的数据类型： ``None`` 。这种特殊的数据类型只有一种可能的取值就是 ``None`` 自身， 而且 **几乎** 不支持任何操作，最常用的用法就是作为占位符，表示 **什么也没有** 或是 **到此为止了** 。

简单程度仅次于 ``None`` 的数据类型是所谓 *布尔* 数据类型，或者叫 *逻辑* 数据类型。这种数据类型仅有2种可能的取值： ``True`` 和 ``False`` 。它们各自的意义正如你在数学或逻辑学中学到的一样： *真* 与 *假* ；所支持的操作也正如你在数学或逻辑学中学到的一样： *与* 、 *或* 还有 *非* 。

.. topic :: Exercise

    猜测下列代码的运行结果，然后运行代码验证你的猜想。

    .. code-block:: python
        :linenos:

            print(True and False)
            print(True or False)
            print(not True and False)
            print(not True or False)

    请尤其注意后两行。

接下来我们要介绍一个与布尔数据类型密切相关的函数： ``bool()`` 。这个函数的特别之处在于，它的输入可以是 **几乎任何** 数据类型，而输出 **永远** 是布尔值（即 ``True`` 与 ``False`` 二者之一）。这种函数也被称为 *类型转换函数* 。

.. topic :: Exercise

    猜测下列代码的运行结果，然后运行代码验证你的猜想。

    .. code-block:: python
        :linenos:

            print(bool(True))
            print(bool(False))
            print(bool(None))


在习题中可以看到 ``None`` 被转换为了布尔值 ``False`` 。习惯上，类似 “不存在、没有、空无一物” 等 **负面** 的概念或状态都对应 ``False`` ，除此之外的情况则对应 ``True`` 。

.. topic :: Exercise

    猜测下列代码的运行结果，然后运行代码验证你的猜想。

    .. code-block:: python
        :linenos:

            print(bool(0))
            print(bool(1))
            print(bool(-1))
            print(bool(''))
            print(bool('abc'))
            print(bool(' '))
            print(bool([]))
            print(bool([1, 2, 3]))
            print(bool([0]))
            print(bool(['']))
            print(bool([None]))
            print(bool([False]))


上面的习题如果你全部做对，可以说是非常了不起了。事实上，如何定义和判断所谓 **负面** 概念往往是微妙而难以把握的。注意上面的运行结果也只在Python世界中成立，其它的编程语言（的作者和支持者）或许有不同的看法。

除了 ``bool()`` 函数，我们再来介绍两个得到布尔值的方法： ``is`` 和 ``==`` 运算符。这两个运算符都是需要2个值作为输入（分别放在左右两边），输出一个布尔值。

先说 ``is`` ，基本上它是与 ``None`` 配套专用的：

.. topic :: Exercise

    猜测下列代码的运行结果，然后运行代码验证你的猜想。

    .. code-block:: python
        :linenos:

            print(None is None)
            print(True is None)
            print(False is None)
            print(0 is None)
            print('' is None)
            print([] is not None)


可以看到除了 ``None is None`` 和 ``[] is not None`` 的结果为 ``True`` ，其余的结果全都是 ``False`` 。也就是说除了 ``None`` 之外的任何值都不是 ``None`` （那简直是一定的）。

虽然这里的结果看起来都是显而易见的，但如果某个值是使用某个（可能不是我们写的）函数得到的，而这个函数可能会用 ``None`` 作为返回值来表示 **什么都没有** ，我们就可以通过 ``f(x) is None`` 来判断能否对这个返回值做进一步操作。前面已经说过， ``None`` 是 **几乎** 不支持任何操作的。


再来说 ``==`` ，注意它与 ``=`` 的区别： ``=`` 用来定义名字， ``==`` 才是用来比较2个值是否相等。如果不小心搞混了 ``=`` 和 ``==`` ，将会导致很可怕的结果！

.. topic :: Exercise

    猜测下列代码的运行结果，然后运行代码验证你的猜想。

    .. code-block:: python
        :linenos:

            print(1 == 1.0)
            print(1/3 == 0.3333333333333333)
            print(len('\n') == 2)
            print('a' == 'A')
            print('b' == 'b ')
            print('C:\\Windows\\System32' == r'C:\Windows\System32')
            print(['a', 'b', 'c'] == ['a', 'b', 'c', 'd'])
            print(['a', 'b', 'c'] == ['c', 'b', 'a'])
            print(None == None)
            print(0 == None)
            print(1 == '1')
            print(1 = 1)


上面的运行结果有2点需要特别说明：

  1. 虽然看起来 ``is None`` 和 ``== None`` 的结果没有区别，但请注意： ``None`` 与其它任何值都属于不同数据类型，而判断不同数据类型的值是否相等是没有意义的。请始终用 ``is`` 来判断某个值是否为 ``None`` 。
  2. 最后的 ``1 = 1`` 显然导致了 **可怕的结果** （你做之前的习题可能已经也遇到过类似的情况），正式名称叫做 *异常* 。这也是一种我们将要介绍的数据类型。


.. note::

    用术语来说，在Python中，比较不同数据类型的值是否相等通常是 **未定义的行为** ，也就是说你不应该依赖这样的运行结果。在其它一些编程语言中，比较不同数据类型的值是否相等，甚至会直接导致 *异常* 。


如果要用一句话总结这一节，那就是“简单”的数据类型也 **并不简单** 。请千万不要掉以轻心。


并不简单的数值
--------------------

终于要说回数值数据类型了。正如你将在本节学到的，数值并不是一种简单的数据类型。

首先是所谓 *整数(int)* 与 *浮点数(float)* 的分别。整数就相当于数学课中的整数，浮点数大致相当于数学课中的小数或分数。

.. note::

    浮点数得名于电脑对小数或分数的特殊存储方式，其细节超出了本书的讨论范围。作最简单理解的话，浮点数是对小数或分数的 **近似** 表示。


在大部分数值运算中，Python不要求你明确区分整数与浮点数，你可以按正常习惯使用。

.. topic :: Exercise

    猜测下列代码的运行结果，然后运行代码验证你的猜想。

    .. code-block:: python
        :linenos:

            print(1 + 2)
            print(1 + 2.5)
            print(1 / 3)
            print(3 / 2)
            print(2 * 1.5)


注意 ``2 * 1.5`` 的结果是浮点数 ``3.0`` 而不是整数 ``3`` 。一般而言，只要参与运算的数值中包含浮点数，结果就是浮点数。即使参与运算的数值全部是整数，运算结果也可能是浮点数（例如除法）。

很自然地，数值之间也可以比较大小，得到布尔值。大小的比较同样允许整数和浮点数的自由组合。

.. topic :: Exercise

    猜测下列代码的运行结果，然后运行代码验证你的猜想。

    .. code-block:: python
        :linenos:

            print(1 < 2)
            print(-1 > -2.5)
            print(1 / 3 >= 0.3)
            print(3.14 <= 22 / 7)
            print(3 / 2 != 1.5)
            print(2 * 1.5 == 3.0)


然而毕竟有一些场合是严格要求只能使用整数或只能使用浮点数的。因此Python分别为两种数值类型提供了类型转换函数。

整数的类型转换函数 ``int()`` 主要有2种用法：

  1. 以字符串作为输入，输出字符串内容所表示的整数
  2. 以数值作为输入，输出将数值进行 **简单取整** 的结果

.. topic :: Exercise

    猜测下列代码的运行结果，然后运行代码验证你的猜想。

    .. code-block:: python
        :linenos:

            print(int('123'))
            print(int('0123'))
            print(int('-123')
            print(int('3.14')
            print(int(3.14))
            print(int(-3.14))
            print(int(1.9))
            print(int(-1.9))
            print(int(' 123 ')


请注意观察 **简单取整** 的结果是否符合你的预期。如果你更习惯四舍五入，可以试试 ``round()`` 函数。

.. note::

    Python还提供了 **向上取整** 和 **向下取整** 。请查阅有关资料了解Python标准库 ``math`` 中的 ``ceil()`` 和 ``floor()`` 函数。


浮点数的类型转换函数 ``float()`` 的主要用法同样有2种：

  1. 以字符串作为输入，输出字符串内容所表示的浮点数
  2. 以数值作为输入，输出该数值的浮点数形式，整数就是在后面添上 ``.0``

.. topic :: Exercise

    猜测下列代码的运行结果，然后运行代码验证你的猜想。

    .. code-block:: python
        :linenos:

            print(float('12.3'))
            print(float('-4.56'))
            print(float('0.333333333333333333333333333333333333'))
            print(float('2.1e5'))
            print(float('3E-4'))
            print(float('-Infinity'))
            print(float(0)
            print(float(-99)
            print(float('1/2 ')

这里可以看到浮点数的形式是多种多样的。诸如 ``'2.1e5'`` ``'3E-4'`` 这样的 **科学计数法** 形式的字符串也可以被转换为浮点数。还有 ``'-infinity'`` 被转换为了 ``-inf``，这是一个表示 **负无穷** 的特殊值，也属于浮点数。这些仅作了解就够了，一般不需要直接用到。

最后说明一下关于浮点数运算的一个违反常识的现象：

.. code-block:: python
    :linenos:

        print(0.1 + 0.2 == 0.3)

结果居然是 ``False`` 。你可以直接 ``print(0.1 + 0.2)`` 从而看到计算结果 ``0.30000000000000004`` ，这是浮点数的特殊近似法则造成的结果。因此如果需要比较浮点数的大小，请务必先用 ``round()`` 或其它方法去掉多余的小数位再进行比较。

.. note::

    Python还提供了进行“符合常识”的数学运算的方法。请查阅有关资料了解Python标准库 ``decimal`` 。

.. note::

    Python还提供了表示和运算复数数据类型的方法。请查阅有关资料了解 ``complex()`` 函数。


列表与集合
--------------------

目前为止我们知道的容器还只有列表一种。我们已经知道了列表的外观特征，以及列表支持的若干操作。

.. code-block:: python
    :linenos:

        names = ['Alice', 'Bob', 'Carol', 'David', 'Emily']
        print(names[0])
        print(names[1:3])
        print(len(names))

现在我们稍微深入的了解一下列表。首先，列表中的元素是可以修改的：

.. code-block:: python
    :linenos:

        names = ['Alice', 'Bob', 'Carol', 'David', 'Emily']
        print('Before:', names[0])
        names[0] = 'Amy'
        print('After:', names[0])

因为 ``names[0]`` 本来是代表一个字符串值，我们可以将其整体看成一个名字。这样就是为这个名字重新指定一个值，应该是很容易理解的。

我们还可以用 ``append()`` 向已有的列表中添加元素：

.. code-block:: python
    :linenos:

        names = ['Alice', 'Bob', 'Carol', 'David', 'Emily']
        names.append('Fred')
        print(len(names))

用 ``extend()`` 的话，可以批量添加多个元素：

.. code-block:: python
    :linenos:

        names = ['Alice', 'Bob', 'Carol', 'David', 'Emily']
        names.extend(['Fred', 'Grace', 'Henry'])
        print(len(names))

注意添加的多个元素要放在列表里作为一个参数。这也可以看做是合并两个列表。

.. topic :: Exercise

    对比下面代码中 ``extend()`` 和 ``append()`` 的结果，说明它们的区别。

    .. code-block:: python
        :linenos:

            names = ['Alice', 'Bob', 'Carol', 'David', 'Emily']
            names.extend(['Fred', 'Grace', 'Henry'])
            names.append(['Fred', 'Grace', 'Henry'])

需要格外注意的是， ``append()`` 和 ``extend()`` 的返回值都是 ``None`` 。经常有人犯迷糊把 ``append()`` 和 ``extend()`` 的返回值当成列表继续进行操作，结果自然是可怕的。

如果我们想去掉列表中重复的元素，可以使用 ``set()`` 函数：

.. code-block:: python
    :linenos:

        nums = [2, 3, 1, 3, 5, 5, 8, 7, 9]
        print(len(nums))
        unique_nums = set(nums)
        print(len(unique_nums))

事实上， ``set()`` 函数是一个类型转换函数，返回的是 *集合（set）* 数据类型。集合数据类型的特性就是不允许包含重复的元素。上面去掉重复元素的方法就是利用这一特性：列表被转换为集合后，多余的重复元素都被丢弃了，此时再用 ``len()`` 得到的就是去重后的元素个数。

集合数据类型的值的外观与列表很像，只是把 ``[]`` 换成了 ``{}`` ：

.. code-block:: python
    :linenos:

        unique_nums = {2, 3, 1, 3, 5, 5, 8, 7, 9}
        print(len(unique_nums))

我们也可以向集合中添加元素，添加单个元素的方法是 ``add()`` ，一次添加多个元素的方法是 ``update()`` ：

.. code-block:: python
    :linenos:

        unique_nums = {2, 3, 1, 3, 5, 5, 8, 7, 9}
        unique_nums.add(4)
        unique_nums.add(2)
        unique_nums.update({9, 10})
        unique_nums.update([5, 15])

.. topic :: Exercise

    请观察上面每行代码执行后 ``unique_nums`` 中的元素个数，并说明个数如此变化的原因。

注意集合的 ``update()`` 的参数可以是集合也可以是列表。其实列表的 ``extend()`` 也允许用集合作为参数。列表和集合并非只有外观相似，很多函数或运算都同时支持列表和集合。例如 ``len()`` 、 ``max()`` 、 ``min()`` 等等。

我们再来介绍一个对列表和集合都能使用的运算符 ``in`` ，作用是判断某个值是否已经存在于列表或集合中，运算的结果当然是布尔值：

.. code-block:: python
    :linenos:

        print(2 in [1, 2, 3])
        print(2 in {1, 2, 3})
        print('Alice' not in {'Alice', 'Bob', 'Carol'})

注意 ``in`` 运算符的左边只能是一个元素，也就是说用 ``in`` 每次只能判断一个元素的存在性。那么如何判断多个元素是否同时存在于列表或集合中呢？

直接在 ``in`` 的左边放上一个列表或者集合是不行的， ``in`` 左边的列表或集合会被作为一个整体参与运算，即只有 ``in`` 右边的容器中的某个元素是与 ``in`` 左边完全相同的列表或集合时，运算结果才会为 ``True`` 。

正确的做法是利用集合的 ``issubset()`` 方法：

.. code-block:: python
    :linenos:

        names = ['Alice', 'Bob', 'Carol', 'David', 'Emily']
        print(set(['Alice', 'Bob']).issubset(names))

如上例所示，利用集合作为中介，判断多个元素是否同时存在于列表中也是可能的。

.. topic :: Exercise

    请尝试说明这个技巧为什么成立。集合还有一个 ``issuperset()`` 方法，请查阅有关资料，然后尝试用 ``issuperset()`` 改写上面的程序。

虽然有很多相似之处，列表和集合毕竟是不同的数据类型，不同之处也有很多。除了 ``append()`` 和 ``add()`` 、 ``extend()`` 和 ``update()`` 这些区别，集合与列表还有两处重要的不同。

首先是 **集合对元素的数据类型有限制** 。例如类似前面习题中出现过的情况：

.. code-block:: python
    :linenos:

        c1 = [1, 2, 3]
        c1.append([4, 5, 6])
        c2 = {1, 2, 3}
        c2.add([4, 5, 6])

其中列表 ``c1`` 被添加了一个列表作为元素，虽然可能不太好理解，但这是完全允许的。对集合 ``c2`` 进行类似的操作却导致出错，也就是说列表是不允许作为一个元素放进集合的。更一般的讲，集合要求放进其中的元素必须是 *hashable* 的。这个词的具体含义我们暂且不讲，就目前已见过的数据类型来说，只有 ``None`` 、布尔值、数值和字符串可以作为元素放进集合。再考虑到实用性，集合中的元素基本只会是数值或字符串。

然后是 **集合不支持用序号来指定元素** ：

.. code-block:: python
    :linenos:

        nums = [2, 3, 1, 3, 5, 5, 8, 7, 9]
        print(nums[0])
        unique_nums = set(nums)
        print(unique_nums[0])

最后一步果然出错了。我们可以用列表的类型转换函数 ``list()`` 将集合转回列表：

.. code-block:: python
    :linenos:

        nums = [2, 3, 1, 3, 5, 5, 8, 7, 9]
        print(nums[0])
        unique_nums = list(set(nums))
        print(unique_nums[0])

这次没有出错。但请注意，在 **列表 - 集合 - 列表** 的转换之后，列表中元素的顺序与原先不同了。这是因为 **集合中的元素是没有顺序的** ，这也是集合不支持用序号指定元素的根本原因。显然，通过序号来修改集合中的元素也是不可能的。

综上，灵活在列表与集合之间互相转换，可以轻松完成许多任务。在利用这些技巧时，请特别注意每步操作中的数据类型，以免出错。另外，如果需要保持列表中各元素的相对顺序不变，就要慎重使用这些技巧。


列表与字典
--------------------

你也许已经注意到，列表中的元素并非必须为同一数据类型。利用这种特性，我们可以用列表表示若干相关数据间的对应关系。例如下例中的列表表示一名学生的考试成绩，第0个元素是姓名，最后的元素表示考试是否通过，中间的元素是各个科目的成绩：

.. code-block:: python
    :linenos:

        student = ['Alice', 85, 90, 77, True]

不只如此，列表中的元素也可以是列表，例如我们可以把上例中的各科成绩合并到列表中作为一个元素：

.. code-block:: python
    :linenos:

        student = ['Alice', [85, 90, 77], True]
        print('Name:', student[0])
        print('Math score:', student[1][0])

这种情况一般叫做 *嵌套* 。注意从嵌套列表的内层列表中取出数据的方法。

嵌套并没有层数的限制。我们可以把多名学生的成绩放进一个更大的列表：

.. code-block:: python
    :linenos:

        students = [
            ['Alice', [85, 90, 77], True],
            ['Bob', [95, 100, 98], True],
            ['Carol', [80, 92, 69], True],
            ['David', [90, 55, 90], False],
            ['Emily', [61, 62, 60], True],
        ]
        print('Name:', students[1][0])
        print('Math score:', students[1][1][0])

上面的例子最后打印出了名为Bob的学生的名字和它的某科成绩。

不难看出，嵌套的列表就像表格一样，可以表示大量的信息。

    +-------+-----------------+--------+
    | Name  | Scores          | Passed |
    |       +-----+-----+-----+        |
    |       |  A  |  B  |  C  |        |
    +=======+=====+=====+=====+========+
    | Alice |  85 |  90 |  77 | True   |
    +-------+-----+-----+-----+--------+
    | Bob   |  95 | 100 |  98 | True   |
    +-------+-----+-----+-----+--------+
    | Carol |  80 |  92 |  69 | True   |
    +-------+-----+-----+-----+--------+
    | David |  90 |  55 |  90 | False  |
    +-------+-----+-----+-----+--------+
    | Emily |  61 |  62 |  60 | True   |
    +-------+-----+-----+-----+--------+


但这里有两点美中不足之处：

  1. 无法直接查到指定学生的成绩，而是必须先知道学生在表中的排列顺序，才能通过序号查出
  2. 反过来，看到 ``scores[1][1][0]`` 这样的代码，也很难看出是哪位学生的哪科成绩

这两个问题都可以通过容器 *字典（dict）* 来解决。

.. code-block:: python
    :linenos:

        student = {'Name': 'Alice', 'Scores': [85, 90, 77], 'Passed': True}


字典的外观和集合相似，是由 ``{}`` 包围起来、由 ``,`` 分隔的多个数据，不同之处在于，字典中的每个元素由 ``:`` 分隔的两个数据组成，这即是所谓 *键值对* 。 ``:`` 之前和之后的数据分别叫做 *键（key）* 和 *值（value）* 。值的部分与列表一样，可以是任何数据类型。键的部分则是与集合一样，可以是任何 **hashable** 的数据，但习惯上只会用字符串作为键。

从字典中取出数据的方法与列表也很相似，是使用 `[]` ，但 `[]` 中不是数字序号而是所需数据的键：

.. code-block:: python
    :linenos:

        student = {'Name': 'Alice', 'Scores': [85, 90, 77], 'Passed': True}
        print('Name:', student['Name'])
        print('Math score:', student['Scores'][1])

可以看到代码的意思表达比之前的列表版本清晰了许多。

字典同样可以 *嵌套* ，也就是把字典作为另一个字典中的值（注意不能作为键）。下面是用字典来表达的学生成绩表：

.. code-block:: python
    :linenos:

        students = {
            'Alice': {'Name': 'Alice', 'Scores': [85, 90, 77], 'Passed': True},
            'Bob': {'Name': 'Bob', 'Scores': [95, 100, 98], 'Passed': True},
            'Carol': {'Name': 'Carol', 'Scores': [80, 92, 69], 'Passed': True},
            'David': {'Name': 'David', 'Scores': [90, 55, 90], 'Passed': False},
            'Emily': {'Name': 'Emily', 'Scores': [61, 62, 60], 'Passed': True},
        }
        print('Name:', students['Bob']['Name'])
        print('Math score:', students['Bob]['Scores'][0])

这个字典中，我们用学生的名字作为键，把存储个人成绩数据的字典作为值，因此可以按名字查到指定学生的成绩数据。一般来说，在字典中，值的部分才是真正有意义的数据，键的部分仅作为查找数据的入口，就好比书籍的目录。

字典的类型转换函数 ``dict()`` 可以把嵌套列表转换为字典，只要嵌套列表符合下面两个条件：

  1. 所有内层列表都有且只有2个元素
  2. 所有内层列表的第0个元素都是hashable的

符合条件的嵌套列表也被称为 *键值对列表* 。

.. topic :: Exercise

    猜测下列代码的运行结果，然后运行代码验证你的猜想。

    .. code-block:: python
        :linenos:

            legs = dict([
                'duck': 2,
                'cow': 4,
                'ant': 6,
                'spider': 8,
            ])
            print(legs['spider'] + legs['cow'])

如果要修改字典中的某个值，方法也和列表类似：

.. code-block:: python
    :linenos:

        c = {'A': 1, 'B': 2, 'C': 3}
        c['B'] = -1
        c['D'] = 4


比列表好的地方在于，如果你指定的键不存在，等号右边的数据就会作为新数据加入到字典中，而不会引发异常。

如果要批量添加数据，可以使用 ``update()`` 方法，输入参数既可以是另一个字典，也可以是一个键值对列表：

.. code-block:: python
    :linenos:

        c = {'A': 1, 'B': 2, 'C': 3}
        c.update({'B': -1, 'D': 4})
        c.update([['A', 0], ['E', 5]])

处理规则和添加单个数据时相同，对已存在的键是修改相应的数据，对不存在的键是添加新数据。


.. topic :: Exercise

    验证上面示例代码对字典数据的添加/修改的结果。注意观察 ``update()`` 的返回值是什么数据类型。

注意无论是单个还是批量，在字典中添加数据和修改数据的方法都完全一致，这也就意味着字典中不可能存在键相同的两个数据（当然也不可能存在多个）。这也是保证能够用键在字典中取到正确数据的必要条件。

.. topic :: Exercise

    猜测下列代码的运行结果，然后运行代码验证你的猜想。

    .. code-block:: python
        :linenos:

            c = {'A': 1, 'B': 2, 'C': 3, 'B': 4}
            print(c['B'])

顺带一提，字典也支持 ``in`` 运算符，但只能用于判断字典中是否已存在某个键，而不能判断字典中是否已存在某个值：

.. code-block:: python
    :linenos:

        c = {'A': 1, 'B': 2, 'C': 3}
        print('B' in c)
        print(2 in c)

这个结果可以看做是把字典中所有的键放进一个集合，然后用这个集合代替字典参与运算得到的。事实上字典的很多操作都可以看做是对其键的集合的操作。

.. topic :: Exercise

    猜测下列代码的运行结果，然后运行代码验证你的猜想。

    .. code-block:: python
        :linenos:

            c = {'A': 1, 'B': 2, 'C': 3, 'B': 4}
            print(len(c))
            print(list(c))

最后总结一下字典的2种重要用途：

  1. 给容器中的每个数据添加名称，有助于明确代码的含义
  2. 通过键快速查到相应的数据，不需要知道数据的排列顺序


列表与字符串
------------

我们已经提到过字符串和列表有一些相似性，例如都可以用 `len()` 函数来得到长度，都可以用 `[]` 取出包含的一个或多个元素（字符）。与此相似，我们既可以用 `in` 运算符来判断列表中是否包含某个元素，也可以用 `in` 运算符来判断字符串中是否包含某个字符：

    ::

        text = 'Hello, world!\n'
        print('o' in text)
        print('x' in text)

如果把字符串看做是由一个个字符组成的列表，这些就都很好理解了。

    ::

        text = ['H', 'e', 'l', 'l', 'o', ',', ' ', 'w', 'o', 'r', 'l', 'd', '!', '\n']
        print('o' in text)
        print('x' in text)

但必须说明，这些相似只是表面现象。字符串是一种单一数据而非容器，与列表有本质的不同。例如我们没法像修改列表中的某个元素那样，修改字符串中的某个字符：

    ::

        text= 'Hello, world!\n'
        text[3] = 'a'

这种操作会引发异常。因此我们至多只能说字符串 **像是** 由一个个字符组成的 *不可修改（Immutable）* 的列表。

甚至，“字符串是字符组成的列表”这种观点也无法解释字符串的 `in` 运算符的更强大一些的用法：字符串的 `in` 运算符左边可以是包含多个字符的字符串，用于判断左边的字符串是否是右边的字符串的一个片段。例如：

    ::

        text = 'Hello, world!\n'
        print('Hell' in text)
        print('World' in text)

这种操作对列表是不成立的：列表的 `in` 运算符左边的数据只能是单个元素，即使把列表放在 `in` 左边，也只会被整体作为一个元素。

既然字符串并不是列表，我们自然也不能用 `append()` 或 `extend()` 来向字符串尾部添加其它字符或字符串。如果想把两个字符串连接起来，我们可以使用 `+` 运算符：

    ::

        a = 'break'
        b = 'fast'
        print(a + b)

屏幕上将会显示 `'break'` 和 `'fast'` 连接得到的新字符串 `'breakfast'` 。注意区分字符串的 `+` 运算与数值的 `+` 运算，二者意义完全不同。数值运算 `1 + 2` 的结果是数值 `3` ，字符串运算 `'1' + '2'` 的结果则是新的字符串 `'12'` ，千万不要将两者混淆。

我们来看一个函数 `say_hello()` ，参数是代表某人名字的字符串，效果是在屏幕上显示对这个人的问候：

    ::

        def say_hello(name):
            greeting = 'Hello, ' + name + '!'
            print(greeting)

在这个函数中，将3个字符串连接得到了问候的内容 `greeting` 。这演示了我们可以将任意多个字符串用 `+` 运算符进行连接。我们可以在函数中加入更多的参数，构造出更灵活的问候语：

    ::

        def say_hello(when, name1, name2):
            greeting = 'Good ' + when + ', ' + name1 + '! ' + name2 + 'is waiting for you.'
            print(greeting)

如果我们调用 `say_hello('morning', 'Alice', 'Bob')` ，屏幕显示的内容将会是 `Good morning, Alice! Bob is waiting for you.` 。

可以看到，这种写法虽然奏效，但参数的增多使得字符串连接的运算变得非常冗长，而且由于内容被大量的 `+` 和 `'` 分隔开来显得支离破碎，也很难看出字符串整体的内容。由于用多个参数来构造格式固定但内容有所变化的字符串，是一种常见又有用的操作，Python为这种场景提供了一个函数 `format()` 。我们可以使用 `format()` 来改写上面的函数：

    ::

        def say_hello(when, name1, name2):
            tmpl = 'Good {}, {}! {} is waiting for you.'
            greeting = tmpl.format(when, name1, name2)
            print(greeting)

在新版本的函数中，我们首先定义了一个包含若干对 `{}` 的字符串 `tmpl` ，这是一个 *模板字符串* ，其中 `{}` 所在的位置代表这里将会被用参数的内容填充。随后我们对 `tmpl` 使用 `format()` 函数，3个参数就依次填充到模板字符串中的3组 `{}` 所在的位置。得到的结果与字符串连接的版本完全一致，但这个使用模板字符串配合 `format()` 的版本显然更整洁清晰。

我们还可以在模板字符串中的 `{}` 中写上参数名，使表意更为清晰：

    ::

        def say_hello(when, name1, name2):
            tmpl = 'Good {when}, {name1}! {name2} is waiting for you.'
            greeting = tmpl.format(when=when, name1=name1, name2=name2)
            print(greeting)

注意这种写法要求 `format()` 函数中的各个参数都要明确写出参数名，也就是像这样带上 `=` 的写法。

使用 `format()` 函数填充模板字符串时， `format()` 的参数并非必须是字符串，我们提到过的各种数据类型都可以用于填充模板字符串。不是字符串的数据，会自动通过字符串的类型转换函数 `str()` 转换为字符串，然后填充到模板字符串的相应位置。数据经 `str()` 转换生成的字符串，通常和我们在Python中表示该数据的写法一致。

.. topic :: Exercise

    猜测下列代码的运行结果，然后运行代码验证你的猜想。

    ::

        print('There is a mile in s{}s.'.format('mile'))
        print('The result of {} + {} is {}'.format(1, 2, 1 + 2))
        print('List: {}'.format(['Alice', 85, 90, 77, True]))
        print('Set: {}'.format({1, 1, 2, 3, 5, 8}))
        print('Dict: {}'.format({'a': 1, 'b': 2}))
        print('Simple values: {} {} {}'.format(True, False, None))
        print('Coordinates: {latitude}, {longitude}'.format(longitude='-115.81W', latitude='37.24N'))
        print('No {code} is good {code}.'.format(code='news'))

最后我们要对字符串的写法做一点补充说明。之前我们一直是用单引号 `'` 来包裹字符串，其实用双引号 `"` 也完全可以：

    ::

        text1 = 'Hello, world!\n'
        text2 = "Hello, world!\n"
        print(text1 == text2)

两种写法效果通常都是完全一致的。但如果字符串本身的内容包含 `'` 或 `"` ，我们就可以从以下4种写法中选择一种：

    ::

        text1 = 'I\'m fine. Thank you!'
        text2 = "I'm fine. Thank you!"
        text3 = "<input id=\"keyword\">"
        text4 = '<input id="keyword">'

一般来说，如果字符串内容中包含单引号 `'` ，我们就用双引号 `"` 来包裹字符串；如果字符串内容中包含双引号 `"` ，我们就用单引号 `'` 来包裹字符串。否则，就需要用 `\'` 或 `\"` 这样带 ``\`` 的写法，以表明这个 `'` 或 `"` 是字符串本身的内容，而非用来包裹字符串。当然如果字符串内容中既包含 `'` 又包含 `"` ，不管我们用 `'` 还是 `"` 包裹字符串，都无法避免带 ``\`` 的写法。注意 `\'` `\"` 与之前介绍过的 `\n` `\t` 一样，都是用2个字符来代表一个字符，也就是所谓 *转义字符* 。

如果字符串内容本身是多行文字，使用转义字符的写法就是在字符串中包含多个 `\n` 。例如：

    ::

        lines = 'The first line.\nThe secord line.\nThe third line.'

一大堆 `\n` 有时也是很影响可读性的。Python也提供了不使用 `\n` 而是还原多行文字本来面貌的写法。例如下面3个字符串的内容完全一致：

    ::

        lines1 = 'The first line.\nThe secord line.\nThe third line.'

        lines2 = '''The first line.
        The secord line.
        The third line.'''

        lines3 = """The first line.
        The secord line.
        The third line."""

使用连续3个引号 `'''` 或 `"""` 来包裹字符串的话，字符串中的换行等特殊字符都会被原样保留，从而最大程度的保留字符串的本来面貌。

Python提供了这么多种字符串的写法，我们该如何选择呢？标准只有一个：请选择使你的代码更 **清晰易读** 的写法。不仅仅是字符串的写法，代码的其它部分，程序设计的整个过程，都需要你保持程序的清晰易读。越是清晰易读的程序，就越不容易出错。


本章小结
--------

本章介绍的几种简单数据类型的对比如下表所示：

    ==================  =======  =================  ==========  ===========  ==============
    数据类型              None          布尔           整数        浮点数         字符串
    ==================  =======  =================  ==========  ===========  ==============
    可取值数量           1         2                 无穷多       无穷多        无穷多
    可取值范围           `None`    `True` `False`    所有整数     所有实数       任何文字内容
    对应 `False` 的值    `None`    `False`           `0`         `0.0`       `''`
    类型转换函数          无        `bool()`          `int()`     `float()`   `str()`
    ==================  =======  =================  ==========  ===========  ==============


本章介绍的3种容器的对比如下表所示：

    =========================  ===================  ===================  ==============================
            数据类型               列表 (list)           集合 (set)          字典 (dict)
    =========================  ===================  ===================  ==============================
    元素数据类型                 无限制                hashable            key要求hashable，value无限制
    元素唯一性                   不限制               是                   key唯一，value不限制
    元素有序性                   支持                 不支持               不支持
    `x in c`                    支持                 支持                 支持
    `len()`                     支持                 支持                 支持
    `sorted()`                  支持                 不支持               不支持
    `max()` / `min()`           支持                 支持                 不支持
    添加单个数据                 `c.append(x)`        `c.add(x)`          `c[k] = v`
    批量添加数据                 `c1.extend(c2)`      `c1.update(c2)`     `c1.update(c2)`
    对应 `False` 的值            `[]`                 `set()`             `{}`
    类型转换函数                  `list()`             `set()`             `dict()`
    =========================  ===================  ===================  ==============================
