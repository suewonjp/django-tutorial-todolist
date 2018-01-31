" vim: sw=2:

set tabstop=4 softtabstop=4 shiftwidth=4 expandtab

let prjPath = expand("%:p:h")

if (filereadable("Session.vim"))
  :source Session.vim
endif

set cpt+=ksrc-symlinks/**

set path=$PWD,$PWD/src-symlinks/**

set wildignore+=tags,memo/**,.git/**,__pycache__/**,*.pyc

nnoremap <silent><leader>w :Ack! --follow -w <C-r><C-w> src-symlinks/<CR>
nnoremap <silent><leader>g :Ack! --follow -w '<C-r>"' src-symlinks/<CR>
nnoremap <silent><leader>/ :AckFromSearch! --follow src-symlinks/<CR>

cnoreabbrev gr Ack! --follow '' src-symlinks/<S-left><left><left><C-r>=EatLastChar()<CR>

