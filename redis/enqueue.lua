
local tags = KEYS[1]
local timestamp = ARGV[1]
local raw_data = ARGV[2]

local unapck_data = cmsgpack.unpack(raw_data)
unapck_data["enqueue"] = "lua" 
local new_data = cmsgpack.pack(unapck_data)
local msg_data = {  
    time = timestamp, 
    tags = tags,
    data = new_data
}

local msg = cmsgpack.pack(msg_data)
redis.call("LPUSH", "data_queue", msg) -- msg queue
return 'field enque worked~'
