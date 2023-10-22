grammar Calculator;

expression
    // important: order of rules matters! look up 'operator precedence' for more info
    : '(' expr=expression ')' #BracedExpr
    | '-' expr=expression #NegExpr
    | left=expression op=('*' | '/' | '%') right=expression #MulExpr
    | left=expression op=('+' | '-') right=expression #AddExpr
    | NUMBER #Num
    ;

NUMBER: [0-9]+('.' [0-9]*)?; // require at least one digit, allow digits behind a decimal point

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines