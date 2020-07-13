<!-- navbar -->
<div class="navbar navbar-default navbar-static-top" role="navigation">
    <div class="container-fluid">
 
        <div class="navbar-header">
            <!-- to enable navigation dropdown when viewed in mobile device -->
            <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            </button>
 
            <!-- Change "Site Admin" to your site name -->
            <a class="navbar-brand" href="<?php echo $home_url; ?>admin/index.php">Admin</a>
        </div>
 
        <div class="navbar-collapse collapse">
            <ul class="nav navbar-nav">

                <li <?php
                        echo $page_title=="Users" ? "class='active'" : ""; ?> >
                    <a href="<?php echo $home_url; ?>admin/views/read_users.php">Users</a>
                </li>

                <li <?php
                        echo $page_title=="News" ? "class='active'" : ""; ?> >
                    <a href="<?php echo $home_url; ?>admin/views/read_news.php">News</a>
                </li>

                <li <?php
                        echo $page_title=="News by category" ? "class='active'" : ""; ?> >
                    <a href="<?php echo $home_url; ?>admin/views/read_news_category.php">News by category</a>
                </li>

                <li <?php
                        echo $page_title=="News by date" ? "class='active'" : ""; ?> >
                    <a href="<?php echo $home_url; ?>admin/views/read_news_date.php">News by date</a>
                </li>

                <li <?php
                        echo $page_title=="Add" ? "class='active'" : ""; ?> >
                    <a href="<?php echo $home_url; ?>admin/operations/add.php">Add</a>
                </li>
                <li <?php
                        echo $page_title=="Update" ? "class='active'" : ""; ?> >
                    <a href="<?php echo $home_url; ?>admin/operations/update.php">Update</a>
                </li>

            </ul>
 
            <!-- options in the upper right corner of the page -->
            <ul class="nav navbar-nav navbar-right">
                <li>
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false">
                        <span class="glyphicon glyphicon-user" aria-hidden="true"></span>
                        &nbsp;&nbsp;<?php echo $_SESSION['firstname']; ?>
                        &nbsp;&nbsp;<span class="caret"></span>
                    </a>
                    <ul class="dropdown-menu" role="menu">
                        <!-- log out user -->
                        <li><a href="<?php echo $home_url; ?>logout.php">Logout</a></li>
                    </ul>
                </li>
            </ul>
 
        </div><!--/.nav-collapse -->
 
    </div>
</div>
<!-- /navbar -->