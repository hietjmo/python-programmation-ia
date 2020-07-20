#!/usr/bin/env runhaskell
-- filter-codeblock-3.hs
import Text.Pandoc.JSON
import Text.Pandoc.Walk
import Data.List.Utils (replace)

-- foldl (\txt (a,b) -> replace a b txt) "abc" [("abc","A"), ("ab","B")]
-- "A"


changeCodeB text =  foldl (\txt (a,b) -> replace a b txt) text [
   ("\n","\n\n"), 
   ("\n>","\n"), 
   ("()"," "), 
   ("["," parentheses quadrate  "), 
   ("{"," parentheses crispe  "), 
   ("]",""), ("|"," "), 
   ("NaN"," non-un-numero "),
   ("&"," ambersand "),
   (" - "," minus "), 
   ("*"," vices "), ("<"," minor que "), (">"," major que ") ]

f :: Block -> Block
f (CodeBlock attr text) = CodeBlock attr (changeCodeB text)
f x = x

g :: Inline -> Inline
g (Code attr text) = Code attr (changeCodeB text)
g x = x

fg :: Pandoc -> Pandoc
fg = walk f . walk g

main = toJSONFilter fg

-- Just use
-- :!chmod +x %

-- pandoc hello-world.md -t plain --filter ./filter-codeblock-3.hs -o hello-world.txt

