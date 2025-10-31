SELECT "receiver_player_name" AS player, COUNT(*) AS receiving_tds
FROM nfl_pbp
WHERE "pass_touchdown" = 1 AND pass=1 -- Use the actual passing TD column
GROUP BY "receiver_player_name"
HAVING COUNT(*) > 0  -- Use COUNT(*) instead of the alias, due to sql evaluation order
ORDER BY receiving_tds DESC;