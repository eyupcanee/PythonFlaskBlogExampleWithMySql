-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Anamakine: 127.0.0.1
-- Üretim Zamanı: 06 Ara 2021, 13:00:07
-- Sunucu sürümü: 10.4.22-MariaDB
-- PHP Sürümü: 8.0.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `flaskblog`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `articles`
--

CREATE TABLE `articles` (
  `id` int(11) NOT NULL,
  `title` text NOT NULL,
  `author` text NOT NULL,
  `content` text NOT NULL,
  `imgurl` text NOT NULL,
  `created_date` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Tablo döküm verisi `articles`
--

INSERT INTO `articles` (`id`, `title`, `author`, `content`, `imgurl`, `created_date`) VALUES
(1, 'Aurora Borealis', 'eyupcan', '<p><strong>Auroras are incredible natural phenomena.</strong></p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p><strong><em>Like This :</em></strong></p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p><strong><em><img alt=\"\" src=\"https://storage.googleapis.com/oceanwide_web/media-dynamic/cache/widen_1600/media/default/0001/34/d737d63c92a62cbfda73c0cd2c352e1139538035.jpeg\" style=\"width: 100%;\" /></em></strong></p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p><strong>You see.Thats Incredible.</strong></p>\r\n\r\n<p>&nbsp;</p>\r\n', 'https://www.xtrlarge.com/wp-content/uploads/2017/03/xtrlarge-aurora-borealis-nasa-roket-1.jpg', '2021-12-06 10:34:07'),
(3, 'Black Hole', 'eyupcan', '<p>Black Holes.</p>\r\n\r\n<p data-placeholder=\"Çeviri\" dir=\"ltr\" id=\"tw-target-text\"><strong>The most elusive thing in human history.</strong></p>\r\n\r\n<p data-placeholder=\"Çeviri\" dir=\"ltr\"><strong>Look At This:</strong></p>\r\n\r\n<p data-placeholder=\"Çeviri\" dir=\"ltr\"><strong><img alt=\"\" src=\"https://cdn.eso.org/images/wallpaper4/black-holes-infographic-v2.jpg\" style=\"width: 100%;\" /></strong></p>\r\n', 'https://www.sciencefriday.com/wp-content/uploads/2019/04/blackhole.jpg', '2021-12-06 11:15:32'),
(4, 'Example', 'example', '<p><b>THIS IS AN EXAMPLE ARTICLE</b></p>\r\n', '', '2021-12-06 11:39:47'),
(5, 'Gaming Pc', 'sarah', '<p>&nbsp;</p>\r\n\r\n<p><strong>You also know that the most important part of a gaming computer is the graphics card.</strong></p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p><strong><img alt=\"\" src=\"https://www.nvidia.com/content/dam/en-zz/Solutions/geforce/geforce-rtx-turing/2080/gallery/geforce-rtx-2080-gallery-c-641-u@2x.jpg\" style=\"width: 100%;\" /></strong></p>\r\n', 'https://images.wallpaperscraft.com/image/single/backlight_neon_electronics_144683_2560x1440.jpg', '2021-12-06 11:46:26'),
(6, 'Python Armstrong Number Algorithm', 'geralt', '<p><strong>This code may work for you:</strong></p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<pre class = \"prettyprint\">\r\nprint(\"\"\"\r\n*************************\r\nArmstrong Number App\r\n*************************\r\n\"\"\")\r\n\r\nnumber = int(input(\"Enter Number\"))\r\na = number\r\nb = number\r\nstep = 1\r\ntotal = 0\r\nwhile (a >= 10):\r\n    a = a / 10\r\n    step += 1\r\n\r\nwhile (b >= 1):\r\n    x = b % 10\r\n    b = int(b / 10)\r\n    total += x**step\r\n\r\nif(number == int(total)):\r\n    print(\"This is a Armstrong Number!\")\r\nelse:\r\n    print(\"This is not a Armstrong Number!\")\r\n\r\n\r\n</pre>\r\n', 'https://st1.myideasoft.com/idea/ct/82/myassets/blogs/python.jpg', '2021-12-06 11:56:35');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `email` text NOT NULL,
  `username` text NOT NULL,
  `password` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Tablo döküm verisi `users`
--

INSERT INTO `users` (`id`, `name`, `email`, `username`, `password`) VALUES
(2, 'Eyüp Can', 'eyxample@gmail.com', 'eyupcan', '$5$rounds=535000$sI1/lnwLWqNWmtAC$APehyg5slWsTUlON4Sb2ItMURneuSC9BFCZdKNVoHS5'),
(3, 'example user', 'example@gmail.com', 'example', '$5$rounds=535000$i0ZYA7aWeU/sT49f$ynKJ7zoGMHyOheBMYNNNX3Wy2Q3p3yblPz9bSa1GNv3'),
(4, 'Sarah Con', 'sarahexample@gmail.com', 'sarah', '$5$rounds=535000$9dghY/eh83gZSx8H$kW2yHUJjhS0F/IZgQfRfBQ0wYihkaj4Sz1MY33pNukB'),
(5, 'Geralt ', 'geraltexample@gmail.com', 'geralt', '$5$rounds=535000$9Ib6I7S1jipEN3u.$yRg893yVFQn7QwU0A5JxWuOO3mApnrdQ4jhzYmelZbA');

--
-- Dökümü yapılmış tablolar için indeksler
--

--
-- Tablo için indeksler `articles`
--
ALTER TABLE `articles`
  ADD PRIMARY KEY (`id`);

--
-- Tablo için indeksler `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- Dökümü yapılmış tablolar için AUTO_INCREMENT değeri
--

--
-- Tablo için AUTO_INCREMENT değeri `articles`
--
ALTER TABLE `articles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Tablo için AUTO_INCREMENT değeri `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
