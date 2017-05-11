class UAEADConverter < EADConverter

  def self.import_types(show_hidden = false)
    [
     {
       :name => "ua_ead_xml",
       :description => "Import UA EAD records from an XML file"
     }
    ]
  end


  def self.instance_for(type, input_file)
    if type == "ua_ead_xml"
      self.new(input_file)
    else
      nil
    end
  end

  def self.profile
    "Convert EAD To ArchivesSpace JSONModel records"
  end

  def format_content(content)
    super.gsub(/[, ]+$/,"") # Remove trailing commas and spaces
  end

  def self.configure
    super


    with 'titleproper' do
      type = att('type')
      case type
      when 'filing'
        set :finding_aid_filing_title, format_content( inner_xml )
      # else
      #   set :finding_aid_title, format_content( inner_xml )
      end
    end

    with 'titleproper/date' do |*|
      set :finding_aid_date, inner_xml

      norm_dates = (att('normal') || "").sub(/^\s/, '').sub(/\s$/, '').split('/')
      if norm_dates.length == 1
        norm_dates[1] = norm_dates[0]
      end
      norm_dates.map! {|d| d =~ /^([0-9]{4}(\-(1[0-2]|0[1-9])(\-(0[1-9]|[12][0-9]|3[01]))?)?)$/ ? d : nil}

      make :date, {
        :date_type => att('type') || 'inclusive',
        :expression => inner_xml,
        :label => att('label') || 'creation',
        :begin => norm_dates[0],
        :end => norm_dates[1],
        :calendar => att('calendar'),
        :era => att('era'),
        :certainty => att('certainty')
      } do |date|
        set ancestor(:resource, :archival_object), :dates, date
      end
    end

    with "langusage/language" do
      set :finding_aid_language, format_content( inner_xml )

    end
  end
end
