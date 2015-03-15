-module(test).
-compile(export_all).

my_hash(_, 0, _, Content) ->
    base64:encode(Content);
my_hash(Algorithm, Iteration, Salt, Content) ->
    Content2 = crypto:hash(Algorithm, <<Salt/binary, Content/binary>>),
    my_hash(Algorithm, Iteration-1, Salt, Content2).
