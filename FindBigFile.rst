编程的基本方法
====================

.. hint::

    阅读本章之前，请先确认你已经熟悉下列概念： ::

        名字（Name） 输入 输出 函数 print 列表 max 引用（import）

    如果有任何疑问，请重新阅读前面的章节。


一种编程方法
--------------------

本章的目的，是让大家掌握一种编程方法。下面给出的这种方法，并不是编程的唯一方法，但我们相信这种固定的、有序的流程，更容易让初学者掌握：

1. 把要处理的问题表示为程序的 *输入* 和 *输出*
2. 确定 *输入* 和 *输出* 的格式，有必要的话，在纸上写几组例子
3. 从输出数据开始向前回溯，将输出数据表示为可以由 **某数据** 经过 **某种操作** 得到

    这里的操作只要有一个 *名字* 表示即可，暂时不需要关心具体细节

4. 上一步中的 **某数据** 如果不是输入数据或已知数据，就继续将它们表示为可以由其它数据经过某种操作得到，直到把输出数据表示成可以由输入数据经过一系列操作得到。

    这里的 **一系列操作** 一般不要超过10个步骤

5. 现在检查将输入数据转换为输出数据所需的一系列操作，这些操作中可以由现有 *函数* 完成的，就直接 *引用*
6. 剩下的不能由现有函数完成的操作，是我们需要实现的新 *函数* 。用同样的步骤分别实现所有这些新函数

这样的抽象描述大概有点难懂。我们仍然用番茄炒蛋的例子来模拟一下：

1. 输入： ``番茄, 鸡蛋, 调料``    输出： ``番茄炒蛋``
2. 略
3. 从输出数据开始向前回溯： ::

    番茄炒蛋 = 炒(切好的番茄, 打好的鸡蛋, 调料)

4. 还没完全回溯到输入数据，继续： ::

    切好的番茄 = 切(番茄)
    打好的鸡蛋 = 打(鸡蛋)

   现在所有的数据都是输入数据了

5. 假设 ``切`` 和 ``打`` 都是现有的函数，只有 ``炒`` 需要进一步实现
6. 我们实现一下 ``炒``：

    输入： ``原料``    输出： ``炒好的菜``

   ::

    热油锅 = 炉灶.加热(锅，油)
    炒好的菜 = 热油锅.翻炒(原料)

大致就是这种感觉。

当然打比方毕竟只是打比方。接下来我们会按上面的方法编写一个真正的程序作为示范。


实例：找出最大文件
--------------------

本节我们要用程序解决一个实际问题。这不但会帮你掌握编程方法，也会帮你写出一个有用的程序：

    找出指定文件夹中最大的一个文件， ``print`` 这个文件的路径和大小

依照上面的流程来处理：

1. 输入： ``一个文件夹``    输出： ``print(文件的路径，文件的大小)``
2. 输入的格式：类似 ``C:\\Windows\\System32``

   输出的格式：类似 ``C:\Windows\System32\abc.txt 12345``
3. 这一步开始就可以直接用代码来写了

    .. code-block:: python

        big_file_path = find_biggest_file(all_files)
        big_file_size = get_file_size(big_file_path)
        print(big_file_path, big_file_size)

4. 还没回溯到输入数据，继续

    .. code-block:: python

        dir_path = r'C:\Windows\System32'
        all_files = list_all_files(dir_path)
        big_file_path = find_biggest_file(all_files)
        big_file_size = get_file_size(big_file_path)
        print(big_file_path, big_file_size)

5. 现在我们需要 ``list_all_files`` 、 ``find_biggest_file`` 、 ``get_file_size`` 这3个操作，来把输入数据转换为输出数据。

   其中 ``get_file_size`` 我们可以直接引用Python标准库：

    .. code-block:: python

        from os.path import getsize as get_file_size

6. 我们只要再实现 ``list_all_files`` 和 ``find_biggest_file`` 就好啦

   关于 ``list_all_files`` 的实现，我们暂时先不讲解。从赠送的 :download:`fileutils.py <fileutils.py>` 中可以直接引用：

    .. code-block:: python

        from fileutils import list_all_files

   需要我们实现的就只剩下 ``find_biggest_file`` 。


到这里我们可以说程序的骨架已经成型，别忘了这些代码是要放进模板的：

    .. code-block:: python

        # coding: utf-8
        """目标：找出指定文件夹下最大的一个文件
        """
        from os.path import getsize as get_file_size

        from fileutils import list_all_files

        def main():
            dir_path = r'C:\Windows\System32'
            all_files = list_all_files(dir_path)
            big_file_path = find_biggest_file(all_files)
            big_file_size = get_file_size(big_file_path)
            print(big_file_path, big_file_size)

        if __name__ == '__main__':
            main()

    .. hint::

        如果想实际运行程序，请把上面的文件保存为 :download:`find_big_file.py <find_big_file.py>` ，并把下载的 :download:`fileutils.py <fileutils.py>` 文件也放到同一目录。


现在来实现 ``find_biggest_file`` 吧。


实现 ``find_biggest_file``
--------------------------

不论实现整个程序，还是实现完成程序中一步操作的函数，我们都用同样的方法和流程：

1. 输入： ``一批文件``    输出： ``其中一个文件``
2. 输入的格式就用列表，比如： ``[r'C:\Windows\System32\abc.txt', r'C:\Windows\System32\def.xml', r'C:\Windows\System32\ghi.png']``

   输出的格式还是类似： ``r'C:\Windows\System32\abc.txt'``

3. 从输出数据开始向前回溯。这里你可能会感觉有点困难，因为输出数据只是从输入数据中拿出一个而已。输出数据与输入数据之间的距离太近，反而不知道该怎么操作？

   这种时候，请回想我们之前是否遇到过类似的函数：从一个列表中拿出一个数据，有这样的函数吗？

   想起来了吗？从列表中找出最大的一个，我们的 ``max`` 函数。我们只要把输入数据的文件列表丢进 ``max()`` ，再告诉 ``max()`` 用文件的大小作为判断标准（ ``key`` ）

   计算文件大小我们前面已经有了 ``get_file_size`` ，这里再用一次即可：

    .. code-block:: python

        file_path = max(file_paths, key=get_file_size)


4. 已经回溯到输入数据了。下一步

5. 我们需要的 ``max`` 和 ``get_file_size`` 函数都已经有了。下一步

6. 没有需要实现的新函数，我们的 ``find_biggest_file`` 函数已经大功告成！

    .. code-block:: python

        def find_biggest_file(file_paths):
            file_path = max(file_paths, key=get_file_size)
            return file_path


回顾整个程序
------------

我们来看下最后写好的程序：

    .. literalinclude:: find_big_file.py
        :language: python
        :linenos:

观察 ``main`` 函数的内部，我们可以清楚看到输入数据经过一系列操作，被转换为输出数据。这正是前面说过的：

    编程就是对数据进行变换与传输。

而我们实际采用的编程方法，实际是由输出数据倒推到输入数据的过程。在这一过程中，我们引入新的名字，然后又对这些名字进行解释，直到所有的名字都可以用电脑已知的数据表示（输入数据和现有函数）。从这个角度看：

    编程就是通过对编程语言进行扩充，向电脑描述和解释问题。

本书中，我们使用Python编程语言，即所谓 *核心语言* 。Python的标准库是对Python语言的扩充，标准库中引入的数千个名字，几乎涵盖了各个领域中常用的概念和操作。在核心语言和标准库的基础上，我们自己编写的程序就是对Python语言的再度扩充，用于描述和解决我们自己的问题。

本章我们解决的是一个小小的问题。后面的章节我们会解决更难一些的问题，你自己的工作和生活中也会遇到更多困难的问题。但只要你能够用程序向电脑将问题描述和解释清楚，电脑就可以帮助你解决。

提升编程水平，也就是提升自己描述和解释问题的能力，这需要经常的练习，也需要多多了解Python语言和标准库中已经准备好的概念和操作。后面的章节会通过一系列实例，帮助你练习编程，顺便为你介绍Python语言和标准库中的一些常用函数。

.. topic:: Exercise 1

    写一个程序，描述本章中的编程方法

.. topic:: Exercise 2

    改写本章完成的程序，计算文件夹中所有文件的总大小

       **提示：** ``sum([1, 2, 3])`` => ``6``

.. topic:: Exercise 3

    改写本章完成的程序，找出文件夹中最大的5个文件

       **提示：** ``sorted([2, 4, 3, 5, 1])`` => ``[1, 2, 3, 4, 5]``
