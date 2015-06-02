class WordCounter

  def initialize(file_name)
    @file = File.read(file_name)
    @words = @file.split
  end

  def count
    @words.length
  end

  def uniq_count
    @words.uniq.length
  end

  def frequency
    words = {}
    @words.each do |word|
      if words.has_key?(word)
        words[word] += 1
      else
        words[word] = 1
      end
    end
    words
  end

end