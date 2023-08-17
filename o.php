<!DOCTYPE html>
<html>
<head>
    <title>عرض الصور في شبكة</title>
    <style>
        body {
            display: flex;
            flex-wrap: wrap;
        }
        .thumbnail {
            width: 150px;
            height: 150px;
            margin: 10px;
            cursor: pointer;
        }
        .thumbnail img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
        .overlay {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.8);
            justify-content: center;
            align-items: center;
            z-index: 9999;
        }
        .overlay img {
            max-width: 90%;
            max-height: 90%;
        }
        .close-btn {
            position: absolute;
            top: 10px;
            right: 10px;
            color: #fff;
            cursor: pointer;
        }
    </style>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script>
        $(document).ready(function () {
            $(".thumbnail").click(function () {
                var imagePath = $(this).find("img").attr("src");
                $(".overlay img").attr("src", imagePath);
                $(".overlay").show();
            });

            $(".close-btn").click(function () {
                $(".overlay").hide();
            });
        });
    </script>
</head>
<body>
<?php
function list_files_recursive($folder_path) {
    $files = array();

    $iterator = new RecursiveIteratorIterator(new RecursiveDirectoryIterator($folder_path));
    foreach ($iterator as $file) {
        if ($file->isFile()) {
            $files[] = $file->getPathname();
        }
    }

    return $files;
}

$root_folder = 'DCIM';
$all_files = list_files_recursive($root_folder);

foreach ($all_files as $file_path) {
    echo '<div class="thumbnail"><img src="' . $file_path . '" alt="' . basename($file_path) . '" /></div>';
}
?>

<div class="overlay">
    <span class="close-btn">X</span>
    <img src="" alt="صورة" />
</div>
</body>
</html>
