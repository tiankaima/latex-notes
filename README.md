# Essays

本`repo`记录了我近期在写的一些用 $ \LaTeX $ 写的文章（大多数是实验报告）

**禁止抄袭、复制、编造实验数据；文章内容中原创部分保留 包括但不限于 出版权、著作权等权利**。

可能文章里存在 $ \LaTeX $ 排版上的问题，欢迎提出宝贵的意见，

同时感谢`ustctug`模板的参考（~~虽然还没机会使用~~）

## Links

* [2022-10-05 A study on Magnetoresistive effect](./13159f/main.pdf)
* [2022-09-25 Medical Physics view on temperature sensors](./6d4ea8/main.pdf)
* [2022-06-04 半导体温度计](./b6fe0c/main.pdf)
* [2022-06-01 基于 SEIR 模型的传染病模拟分析](./c0511f/main.pdf)
* [2022-05-29 磁力摆](./f33ea2/main.pdf)
* [2022-05-24 针对 ACG 风格图像识别算法的一种改进和应用](./8205e2/main.pdf)
* [2022-05-21 切变模量的测量](./631f07/main.pdf)
* [2022-05-16 衍射实验](./8b7dcb/main.pdf)
* [2022-05-09 拉伸法测量钢丝的杨氏模量](./3bb37f/main.pdf)
* [2022-04-29 （private）~~石墨烯的电学性质及其应用~~](./095998/main.pdf)
* [2022-04-23 整流滤波电路及应用](./89e0dc/main.pdf)
* [2022-04-17 分光计的调节和使用](./47a54b/main.pdf)
* [2022-03-28 声速的测量](./a81fd6/main.pdf)
* [2022-03-21 光电效应实验](./0f7b67/main.pdf)
* [2022-03-14 自由落体测重力加速度](./70be0b/main.pdf)
* [2022-03-14 单摆法测重力加速度](./4ed5e0/main.pdf)

## Change Log

### 2022/10/05 更新

时隔半年左右的再一次更新……其实并不是这段时间内没有写什么内容，而是都没有同步上来（笑），这一段时间感觉自己颓废了不少呢……

我现在对大物实验倒也没那么反感了（可能我这学期也就只有四次实验课的缘故罢，好了伤疤忘了疼的感觉www），起码这个经历让我练会了 $ LaTeX $ 的使用，起码背下来了一些符号的使用……奉劝学弟学妹还是不要轻视这门课程，有什么事情可以联系我。

更新的内容如下：

* 添加了`newfolder.py`文件，后续用cli直接添加文件夹，省去一步操作。
* 重新把`*.pdf`文件放上来了，方便GitHub阅读一点罢
* 修改了`.vscode`一些规则，缓存文件眼不见心不烦……文章目录的问题我再思考一下
* 重新补足了一些链接……在考虑怎么自动添加链接，毕竟这个repo会一直更新下去的，手动还是太麻烦了wwww
* 之前写的`CHANGELOG`好羞耻……好想删掉

### 2022/4/13 更新

[2022-03-28 声速的测量](./a81fd6)

这个实验当时做起来十分拉跨……现在想想当时干了很多傻事，而且我那个仪器的摇轮还是坏的……麻了。最后固体（黄铜棒、有机玻璃棒）的那两个建议多测几次，不然分数也不会高……

### 2022/3/31 更新

更新了文件目录的更新规则（~~万一明年还要继续写呢……~~）

### 2022/3/27 更新

[2022-03-22 光电效应实验](./0f7b67)（大雾A标准，包含补偿法实验内容）

感谢@hkxa0933 的帮助，阿里嘎多。

 > 这个实验应该是2022/3/21做的，然后第二天开始动笔，于是目录就很随意地用了`0322`这个名字……
 >
 > 做这个实验的时候，给一点小建议：带个**支架，拿手机把实验数据录下来**（不是大雾A的话可能不需要），补偿法最后有大概500个数据点……自动的话，每个数据就只有1s的时间记录；为了速度的话，建议现场能记多少是多少，没记录完整地回来看回放。
 >
 > > 或者学我用GoPro也行……（草）

做实验其实没什么需要特别注意的（不过有的时候需要考虑一下是不是自己实验仪器有问题，因为真的可能有问题，发现不对劲的时候及时举手提问……老师在旁边会帮你的）

处理实验数据的时候简单地线性回归就行，不用自己写代码。

> 这次我把用的`jupyter notebook` 贴出来了，前两个代码不想找了……也没什么特别难的

在一些特殊的地方可以先用 $ \log $ 处理一下，再回归分析。

[2022-03-18 自由落体测重力加速度](./70be0b)

[2022-03-15 单摆法测重力加速度](./4ed5e0)

感谢@Thomas Hu的帮助（~~关于我什么准备都没做然后空手去一教是否做错了什么事情~~）

> 实验时间：2022/3/14，不过报告写起来稍微麻烦一点（主要是刚开始使用 $ \LaTeX $ 排版……熟悉一点就好了）
>
> > $ \LaTeX $ 排版并不是必须；如果你实验报告肝不完了可以用Word套用一下模板；不过为了工整最好还是用 $ \LaTeX $ 排一下吧……看起来会更整洁一点。
>
> 这个实验里要求不确定度分析……所以尽量多测几次摆长（不要事后编数，隔一段时间多测几次，不会累死人的……）

稍微注意一下：光电门测量重力加速度的时候，由于电磁铁上面有剩磁（延时下落），所以 $ t_1,t_2 $ 这两个数据都不能用；必须用 $ t_2 - t_1 $ 来处理。

数据处理和绘图拿Python就够了……而且默认的参数基本不用调（如果你没时间的话）

不过没整理代码……下次一定，这次就算了吧（小声）
