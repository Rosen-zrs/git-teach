# Git Tutorial

[TOC]

## Why Git?

​	Git是一个涵盖非常多功能的版本管理器，作为现代程序猿的必备技能，我们常使用它来管理代码仓库。

+ 多版本管理

  + 不使用git

    ![](https://content.markdowner.net/pub/BLxnO6-doDLgY9)

  + 使用git

    ![](https://content.markdowner.net/pub/2jQWMz-EGQNj1e)

## 准备

+ Git bash(Windows系统)/ Git(Linux/Mac os)

+ Github/Gitee账户

+ VsCode（推荐）

首先要绑定本地 Git 的邮箱与账户(Github账户的邮箱与名称):

```bash
git config --global user.email "you@example.com"

git config --global user.name "Your Name"
```



## 本地



### 仓库初始化

+ 仓库是什么？

  可以理解为git能够识别的目录

  

+ **实践**

```bash
git init
ls -a
```

我们会发现，相比于初始化前，目录下多了一个**.git**目录，该目录记录版本之间的差异。



### 查看状态与添加文件

对于一个仓库来说,最基本的事情有两件:

```bash
# 查看仓库
git status

# 添加文件
git add [file path]
git commit -m "备注信息"
```

+ **git**所有的工作都是依托于.git/目录的

### 工作区与暂存区

![](https://content.markdowner.net/pub/Avo13X-BzanrpA)

工作区非常简单,就是我们所在的这个目录，那么后面这个 版本库 是什么东西呢。因为工作区的内容与 Git 所跟踪的内容是分开的, Git 仅能识别出:

1. 它跟踪的文件与当前的文件夹文件的区别(哪些没有跟踪到)

2. 跟踪文件内容发生的变化

而暂存区就是git通过添加指令后文件储存的区域，git跟踪的是暂存区中的文件，而不是工作区的文件。



+ **实践**

首先，我们查看仓库状态

```bash
git status
```

![](https://content.markdowner.net/pub/7WaGwq-LQ3kgad)

我们可以看到：

1. 当前在分支 master 上
2. 仓库没有过 commit(提交)记录
3. 没有跟踪到的文件

添加文件，再次查看仓库状态

```bash
git add .
git status
```

![](https://content.markdowner.net/pub/Q7kQWx-Rg6joo1)

此时文件已经被添加入暂存区，git可以跟踪到。



### 提交

git通过提交指令将暂存区中的文件传到分支上，此处的分支为master。

```bash
git commit -m "first commit"
```

![](https://content.markdowner.net/pub/DAoVe6-E8Xd0)

我们可以对main.py进行修改，将主函数中调用的add函数改成multiply，并保存

此时我们再次查看状态，显示并未跟踪，因为我们没有将修改过的文件变化添加入暂存区

![](https://content.markdowner.net/pub/m5BzAx-a8x1vmw)

```bash
git add .
git commit -m "second commit"
```

我们可以查看到文件的改变信息。

+ 查看提交记录

```bash
git log
```

![](https://content.markdowner.net/pub/Q7kQGG-EvrA866)

通过这个命令,我们可以看到我们之前所有的提交记录,包括 这次提交的ID,提交人,具体的时间,提交的名称。

这里说到节点的概念,对于 Git 来说,它的管理思想是运用了**树**的思想,对于所有的提交,均会产生一个节点,这个节点记录了当前节点对上一个节点的变化。

那么我们直接将所有的变化按照顺序叠加起来就能得到当前仓库的状态了,通俗的说就是 Git 记录了变化的变化。

目前我们的仓库有两个节点：
$$
Root \Rightarrow first \quad commit   \Rightarrow second \quad commit
$$

+ 返回节点

```bash
git reset
```

```bash
git reset 'commit_id' --hard(--hard是指工作区,暂存区,分支均退回到上一个节点的状态)
```

如果用 --hard 的版本回退是单向树的行为,回退后版本不可恢复，可以了解一下：

```bash
git reset commit_id --mixed/--soft
```



## 远程

+ 创建远程仓库，并关联

```bash
git remote add origin [远程地址]
```

+ 上传分支

```bash
git push -u origin master
```

+ 下拉分支

```bash
git pull origin master
```

+ 冲突

  在很多时候git可以自动帮我们合并代码解决，但如果在开发过程中同一部分代码经过多人修改，就需要手动解决冲突。

  + 本地有与远程不同的未提交修改：

    先使用指令`git stash`将修改藏匿，然后使用指令`git merge <remote>/<branch>`与远程最新的修改合并。

    关于藏匿的内容呢，可以使用命令`git stash apply`应用最近的藏匿，这时Git会自动合并，如果存在冲突则需要你手动处理。如果需要更旧的藏匿找到它并应用，如：

    ```bash
    $ git stash list
    stash@{0}: WIP on main: 20cc20b maomao conflict
    stash@{1}: WIP on main: cfd8fca resolved conflict
    stash@{2}: WIP on main: 7f55a97 modified README.md too
    
    $ git stash apply stash@{1}
    Auto-merging README.md
    CONFLICT (content): Merge conflict in README.md
    ```

    

  + 本地有与远程不同的已提交修改：

    使用指令`git merge <remote>/<branch>`与远程最新修改合并，这时会告诉你合并失败要求手动修改对应文件，如：

    ```bash
    $ git merge origin/main
    Auto-merging README.md
    CONFLICT (content): Merge conflict in README.md
    Automatic merge failed; fix conflicts and then commit the result.
    ```

    打开对应文件，修改冲突的内容，并再次提交。

+ 拉取分支数据

```bash
git fetch [remote]
```

也是访问远程仓库，从中拉取所有你还没有的数据，但是它只会将数据下载到你的本地仓库而不会进一步自动合并或修改你当前的工作。

+ 合并分支

```bash
git merge origin/master
```

其实`git pull`就是`git fetch` + `git merge`。



### ssh-key免密登录

+ 生成公钥和私钥

```bash
ssh-keygen -t rsa -C "Your Email"
```

将/.ssh文件夹中的id_rsa.pub中的公钥复制到github网站中个人账户设置的ssh-key中



![](https://content.markdowner.net/pub/P71BRO-pwMWMnm)



### 分支

在开发过程中，如果我们想进行新功能的开发，又不想影响到当前的版本，我们可以使用分支功能。

+ 创建分支

```bash
git branch [branch name]
```

+ 查看分支

```bash
git branch  (-a)
```

+ 切换分支

```bash
git checkout [branch name]
```

等到分支开发完成后，我们可以将其与主分支进行合并

+ 合并分支

```bash
git merge [branch name]
```

+ 删除分支

```bash
git branch -d [branch name]
```





## .gitignore

很多时候我们不希望将编译文件或者视频上传到远程仓库，注意git是版本管理工具，不是云盘！！！

所以我们可以通过.gitignore文件指定文件，让git自动忽略它

```
.vscode
build
Camera
*.avi
*.mp4
*.png
*.csv
*.jpg
data
hotspot
```



## 其他常用的git指令

+ 克隆仓库

```bash
git clone [仓库地址]
```

+ 删除文件

```bash
git rm file
```

+ 重命名文件

```bash
git mv oldFileName newFileName
```

+ 新建标签并上传

```bash
git tag +标签名称
git push [remote] [tag]
```















