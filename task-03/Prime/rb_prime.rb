list = [2]
limit = gets.chomp.to_i
(2..limit).each do |i|
    c = list.length
    a = 0
    list.each do |j|
        if i % j != 0
            a+=1
        else
            next
        end
    end
    if a == c
        list << i
    end
end

list.each { |i| puts i }
