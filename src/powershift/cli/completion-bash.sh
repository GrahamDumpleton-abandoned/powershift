_powershift_completion() {
    COMPREPLY=( $( env COMP_WORDS="${COMP_WORDS[*]}" \
                   COMP_CWORD=$COMP_CWORD \
                   _POWERSHIFT_COMPLETE=complete $1 ) )
    return 0
}

complete -F _powershift_completion -o default powershift;
