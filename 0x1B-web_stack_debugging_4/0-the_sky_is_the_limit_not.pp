# A puppet manuscript to replace a line in a file on a server
exec { 'set limit to 2000':
  path    => '/bin',
  command => "sed -i 's/15/2000/' /etc/default/nginx"
}
exec { 'reboot nginx':
  command => '/usr/sbin/service nginx restart'
}
