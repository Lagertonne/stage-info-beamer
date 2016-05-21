gl.setup(1280, 720)

util.resource_loader {
	"bg.png",
	"fL.png",
	"fR.png",
	"shader.vert",
	"shader.frag",
}

bL = false
bR = false

--[[ util.data_mapper{
	["fl_on"] = function() 
		fL = true
		print("Buzzer L")
	end;

	["fl_off"] = function()
		fL = false
		print("Buzzer R")
	end;
} --]]

node.event("data", function(data, suffix)
	print("input was: " .. data)
	if data == "bl_on" and bR == false then
		bL = true
	elseif data == "br_on" and bL == false then
		bR = true
	elseif data == "bl_off" then
		bL = false
	elseif data == "br_off" then
		bR = false
	end
end)

function node.render()
	gl.clear(0,0,0,0)
	bg:draw(0, 0, 1280, 720)
	if (bL == true) then
		fL:draw(0, 0, 1280, 720)
	end
	if (bR == true) then
		fR:draw(0, 0, 1280, 720)
	end

end
