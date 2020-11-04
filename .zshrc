# zsh config
export ZSH_THEME='philips'
source /home/theo/.config/.oh-my-zsh/oh-my-zsh.sh
/usr/bin/setxkbmap fr 
/usr/bin/xset -b
alias left=' xrandr --output HDMI-A-0 --left-of eDP'
alias setup='sudo cryptsetup luksOpen /dev/sdb2 data; sudo mount /dev/mapper/data /Data'
