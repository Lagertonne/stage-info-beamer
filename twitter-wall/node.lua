gl.setup(1280, 720)
local json = require "json"

font = resource.load_font("arial.ttf")

-- Wrap Function is taken from
-- https://github.com/dividuum/info-beamer-nodes/blob/master/29c3-twitter/node.lua
-- At line ~53

function wrap(str, limit, indent, indent1)
	limit = limit or 35 
    local here = 1
	local wrapped = str:gsub("(%s+)()(%S+)()", function(sp, st, word, fi)
	    if fi-here > limit then
		    here = st
            return "\n"..word
        end
    end)
    local splitted = {}
    for token in string.gmatch(wrapped, "[^\n]+") do
	    splitted[#splitted + 1] = token
    end
    return splitted
end


util.file_watch("tweets.json", function(content)
	tweets = {}
	for idx, tweet in ipairs(json.decode(content)) do
		tweet.lines = wrap(tweet.text, 60)
		tweets[#tweets+1] = tweet
	end
	return tweets
end)

--[[ util.data_mapper{
    ["add"] = function(data)
        print(data)
        local tweet = json.decode(data)
	        tweet.screen_name = "@" .. tweet.user
	        --tweet.profile_image = resource.load_image_async(tweet.profile_image)
	        --if tweet.background_image then
	            -- tweet.background_image = resource.load_image_async(tweet.background_image)
	        --end
	        --tweet.text = wrap(tweet.text, 27)
	        -- tweet.created_at = sys.now() - tweet.age
	        table.insert(tweets, tweet)
	        if #tweets > 10 then
		        table.remove(tweets, 1)
		    end
	end
} ]]--



function node.render()
	gl.clear(0, 0, 0, 0)
	a = 16
	LineSize=45
	UserSize=50
	for tweetsC = 1, 10 do
		font:write(16, a, tweets[tweetsC].user, UserSize, 0.5,1,1,1)
		for idx, line in ipairs(tweets[tweetsC].lines) do
			font:write(16, a+LineSize+5, line, LineSize, 1,1,1,1)
			a=a+LineSize
		end
		a = a + UserSize+LineSize + 10
	end
end
