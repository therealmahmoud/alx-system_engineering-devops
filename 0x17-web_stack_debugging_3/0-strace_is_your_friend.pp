# Fixing internal server error 500.
exec { 'Fix apache':
  command  => 'sudo sed -i "s/.phpp/.php" /var/www/html/wp-settings.php',
  provider =>  shell,
}
