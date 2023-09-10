list = [2]
limit = gets.chomp.to_i
if limit == 1 
    puts "no prime"
elsif limit == 2
    puts 2
elsif limit == 0
    puts "no prime"
else
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
end