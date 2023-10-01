import arcpy, datetime
arcpy.env.overwriteOutput = True
workspace = r"C:\Sternberger\LOCAL_GPS_DATA_TEST\Wylie Ridge-Cecil\Working.gdb"
ENV_GDB = r"C:\Sternberger\LOCAL_Wiley_Ridge_TEST\Env_gdb\COPY_TEST_Wiley_COPY.gdb\Env_Field_Data"

start_time = datetime.datetime.now()
print("Start time: " + str(start_time))
#Streams
##########################################################################################################################################################################################################################################
##########################################################################################################################################################################################################################################
##########################################################################################################################################################################################################################################
#Assign stream points (for various streams) shapefile to variable STREAM
STREAM = r"C:\Sternberger\LOCAL_GPS_DATA_TEST\Wylie Ridge-Cecil\data\Merged\Wylie_STREAM_merge.shp"
#Create blank lists to store stream IDs and stream IDs for post processing review (including an exclusive list for extentions of previous features). 
Stream_IDs = []
Stream_IDs_REVIEW = []
EXT_list = []
ext = 'ext'

#Initialize attribute field lists for features.
stream_att_list = [('Project_Name', 'TEXT','','', '50','','',''),('GAI_ID', 'TEXT','','', '16','','',''), ('Stream_Type', 'TEXT','','', '16','','',''),
                               ('Bank_Width_Feet', 'DOUBLE','','','','','',''),('GPS_Date', 'DATE','','','','','',''), ('Mod_Date', 'DATE','','','','','',''),('Latitude', 'DOUBLE','','','','','',''),
                               ('Longitude', 'DOUBLE','','','','','',''), ('Impacted?', 'TEXT','','', '50','','',''), ('RC_ID', 'TEXT','','', '50','','',''), ('SWW_ID', 'TEXT','','', '8','','',''),
                               ('Floodway_Buffer', 'DOUBLE','','','','','',''), ('Comment', 'TEXT','','', '50','','',''), ('Stream_Nam', 'TEXT','','', '50','','',''),
                               ('CR_Intersect?', 'TEXT','','', '8','','',''), ('Quality_Use_Description', 'TEXT','','', '24','','','')]

#Append all STREAM points into ENV_GDB
#arcpy.Append_management(STREAM, ENV_GDB +"\Stream_Flags", "NO_TEST", field_mapping='Project_Name "Project_Name" true false false 24 Text 0 0 ,First,#;GAI_ID "GAI_ID" true false false 16 Text 0 0 ,First,#,STREAM,GAI_ID,-1,-1;Flag_Num "Flag_Number" true false false 2 Short 0 0 ,First,#,STREAM,Flag_Num,-1,-1;Type "Stream_Type" true false false 16 Text 0 0 ,First,#,STREAM,Type,-1,-1;Bank_Side "Bank_Side" true false false 12 Text 0 0 ,First,#,STREAM,Bank_Side,-1,-1;Bank_Width "Bank_Width_Feet" true false false 8 Double 0 0 ,First,#,STREAM,Bank_Width,-1,-1;Flag_Type "Flag_Type" true true false 16 Text 0 0 ,First,#,STREAM,Flag_Type,-1,-1;Culvert "Culvert?" true true false 8 Text 0 0 ,First,#,STREAM,Culvert,-1,-1;Culvert_Ty "Culvert_Type" true true false 8 Text 0 0 ,First,#,STREAM,Culvert_Ty,-1,-1;Culvert_Si "Culvert_Size_Inches" true true false 2 Short 0 0 ,First,#,STREAM,Culvert_Si,-1,-1;Culvert_Ma "Culvert_Material" true true false 12 Text 0 0 ,First,#,STREAM,Culvert_Ma,-1,-1;Parallel_C "Parallel_Culvert?" true true false 8 Text 0 0 ,First,#,STREAM,Parallel_C,-1,-1;Bridge "Bridge?" true true false 8 Text 0 0 ,First,#,STREAM,Bridge,-1,-1;GPS_Date "GPS_Date" true true false 8 Date 0 0 ,First,#,STREAM,GPS_Date,-1,-1;Comment "Comment" true true false 50 Text 0 0 ,First,#,STREAM,Comment,-1,-1;Stream_Nam "Stream_Name" true true false 50 Text 0 0 ,First,#,STREAM,Stream_Nam,-1,-1', subtype="")

#Below draws the stream lines based upon the gps points taken and will ultimately append them into the ENV_GDB
#Create a list of stream features to iterate through.
GAI_ID_count = 0
with arcpy.da.SearchCursor(STREAM, "GAI_ID") as cursor:
    for row in cursor:
        if row[0] not in Stream_IDs:
            Stream_IDs.append(row[0])
            GAI_ID_count += 1
print((str(GAI_ID_count) + " unique GAI IDs."))
print(Stream_IDs)
unique_ID = 1
#print("Stream count: " + str(arcpy.GetCount_management(Stream_IDs).getOutput(0)))

#As a first check, account for IDs that are extentions of previous features. These will likely need to be manually adjusted. 
#with arcpy.da.SearchCursor(STREAM, "GAI_ID", '"GAI_ID" LIKE' + "'%s'" %ext) as cursor:
    #for ID in cursor:
        #EXT_list.append(ID[0])

#Iterate through each grouping of features (GAI_ID), draw the feature, transfer attributes to the derived feature, and append the feature into the ENV_GDB. 
for ID in Stream_IDs:
    print(ID)
    ID_original = str(ID)
    ID_replace_one = ID_original.replace(" ", "_")
    ID_replace_final = ID_replace_one.replace("-", "_")
    stream_lyr = arcpy.MakeFeatureLayer_management(STREAM, "stream_lyr", where_clause='"GAI_ID" =' + "'%s'" %ID)
    print("stream lyr count: " + str(int(arcpy.GetCount_management(stream_lyr).getOutput(0))))
    #Make a blank list for flag nums to make sure each number occurs only once. If more than one flag has the same number, add to Stream_IDs_REVIEW.##################################################################################### 
    stream_lyr_flagnums = []
    bank_num = []
    with arcpy.da.SearchCursor(stream_lyr, "Bank_Side") as cursor:
        for row in cursor:
            if row[0] not in bank_num:
                bank_num.append(row[0])
    with arcpy.da.SearchCursor(stream_lyr, "Flag_num") as cursor:
        for row in cursor:
            if row[0] not in stream_lyr_flagnums:
                stream_lyr_flagnums.append(row[0])
            else:
                if len(bank_num) == 1:
                    print("Feature " + str(ID) + " needs reviewed. More than one flag has the same number. Adding ID to review list")
                    Stream_IDs_REVIEW.append(ID)
                    break
                else:
                    stream_lyr_flagnums.append(row[0])
    #Check to make sure there are at least two points for the feature to be drawn from.
    #Test to make sure flags increase sequentially by an interval of 1. If not, its possible a flag was missed. Add to Stream_IDs_REVIEW if not.######################################################################################## 
    length_flagnums = len(stream_lyr_flagnums)
    if length_flagnums == 1 and ID not in Stream_IDs_REVIEW:
        print("Feature " + str(ID) + " consists of only one point. A stream cannot be drawn. Adding ID to review list.")
        Stream_IDs_REVIEW.append(ID)
    max_flagnums = max(stream_lyr_flagnums)
    #If biggest number in list flag nums is not also the length of the list, this implies that a flag number was skipped (flag nums do not all increase by interval of one)
    if max_flagnums > length_flagnums and ID not in Stream_IDs_REVIEW:
        print("Feature " + str(ID) + " needs reviewed. Flag numbers do not all increase by interval of one. A flag may have possibly been skipped or querried out. Adding ID to review list.")
        Stream_IDs_REVIEW.append(ID)
    

    #Loop through and draw streams.####################################################################################################################################
    if ID not in Stream_IDs_REVIEW:
        try:
            #######Draw a stream in order of current Flag_num.
            #Initialize list of streams to attribute
            att_stream = []
            print(str(ID_replace_final) + "uID_" + str(unique_ID))
            unique_ID += 1
            stream_line = arcpy.PointsToLine_management(stream_lyr, workspace + "\stream_line_" + str(ID_replace_final) + "uID_" + str(unique_ID), Line_Field = "Bank_Side", Sort_Field = "Flag_num", Close_Line = "NO_CLOSE")
            att_stream.append("stream_line")
            ####Additionally, account for streams drawn in reverse order.
            #Set coincidence test variables.
            downstream_center, upstream_center, downstream_left, upstream_left, downstream_right, upstream_right = True, True, True, True, True, True
            #Create end and start point features for coincidence test.
            end_point = arcpy.FeatureVerticesToPoints_management(stream_line, workspace + "\end_point_" +str(ID_replace_final) + "uID_" + str(unique_ID), "END")
            start_point = arcpy.FeatureVerticesToPoints_management(stream_line, workspace + "\start_point_" +str(ID_replace_final) + "uID_" + str(unique_ID), "START")
            #If there is one end point (and therefore one start point), we know that only one line was drawn for the ID (likely center bank but possibly only one of two double bank data provided). If one
            #line, run the downstream-end point/upstream-start point coincidence test as usual. If there is more than one end point, this means that there was more than one line drawn, which implies it is
            #right/left bank. Make feature layer of each bank, and run coincidence test seperately for each line. Otherwise, the coincidence test has the potential to be invalid in particular instances.
            end_pt_cnt = int(arcpy.GetCount_management(end_point).getOutput(0))
            if end_pt_cnt == 1:
                print("1 end point")
                #Check downstream-end point coincidence.
                arcpy.SelectLayerByLocation_management(stream_lyr, "ARE_IDENTICAL_TO", end_point)
                with arcpy.da.SearchCursor(stream_lyr, "Flag_type") as cursor:
                    for t in cursor:
                        if t[0] == "Upstream/start" or t[0] == "Headcut":
                            downstream_center = False
                            print("downstream center is false")
                #Check upstream-start point coincidence.
                arcpy.SelectLayerByLocation_management(stream_lyr, "ARE_IDENTICAL_TO", start_point)
                with arcpy.da.SearchCursor(stream_lyr, "Flag_type") as cursor:
                    for t in cursor:
                        if t[0] == "Downstream/End" or t[0] == "Confluence":
                            upstream_center = False
                            print("upstream center is false.")
            else:
                #Make sub feature layers of just right and just left STREAM points from stream_lyr.
                print("more than one end point")
                stream_lyr_left = arcpy.MakeFeatureLayer_management(stream_lyr, "stream_lyr_left", where_clause="Bank_Side = 'Left'")
                stream_lyr_right = arcpy.MakeFeatureLayer_management(stream_lyr, "stream_lyr_right", where_clause="Bank_Side = 'Right'")
                ##Left Bank coincidence test.
                #Downstream coincidence.
                arcpy.SelectLayerByLocation_management(stream_lyr_left, "ARE_IDENTICAL_TO", end_point)
                with arcpy.da.SearchCursor(stream_lyr_left, "Flag_type") as cursor:
                    for t in cursor:
                        if t[0] == "Upstream/Start" or t[0] == "Headcut":
                            downstream_left = False
                            print("downstream left is false")
                            
                #Upstream coincidence
                arcpy.SelectLayerByLocation_management(stream_lyr_left, "ARE_IDENTICAL_TO", start_point)
                with arcpy.da.SearchCursor(stream_lyr_left, "Flag_type") as cursor:
                    for t in cursor:
                        if t[0] == "Downstream/End" or t[0] == "Confluence":
                            upstream_left = False
                            print("upstream left is false.")
                ##Right bank coincidence test
                #Downstream coincidence.
                arcpy.SelectLayerByLocation_management(stream_lyr_right, "ARE_IDENTICAL_TO", end_point)
                with arcpy.da.SearchCursor(stream_lyr_right, "Flag_type") as cursor:
                    for t in cursor:
                        if t[0] == "Upstream/Start" or t[0] == "Headcut":
                            downstream_right= False
                            print("downstream right is false")
                #Upstream coincidence
                arcpy.SelectLayerByLocation_management(stream_lyr_right, "ARE_IDENTICAL_TO", start_point)
                with arcpy.da.SearchCursor(stream_lyr_right, "Flag_type") as cursor:
                    for t in cursor:
                        if t[0] == "Downstream/End" or t[0] == "Confluence":
                            upstream_right = False
                            print("upstream right is false.")
                arcpy.SelectLayerByAttribute_management(stream_lyr_left, "CLEAR_SELECTION")
                arcpy.SelectLayerByAttribute_management(stream_lyr_right, "CLEAR_SELECTION")
                        
                                
            #If line is single bank and passes coincidence test, attribute and append into data base. If line is single bank but does not pass coincidence test, draw in reverse order, then attribute and append into data base. 
            if end_pt_cnt == 1:
                if downstream_center == True and upstream_center == True:
                    #Add attribute fields to stream_line from STREAM points
                    for att in stream_att_list:
                        arcpy.AddField_management(*(stream_line,)+att)
                    #Update values of stream_line with values from stream_lyr points.
                    #Start editing
                    edit = arcpy.da.Editor(workspace)
                    edit.startEditing(False, True)
                    edit.startOperation()
                    update_fields = ["GAI_ID", "Type", "Bank_Width", "Stream_Nam", "GPS_Date"]
                    with arcpy.da.SearchCursor(stream_lyr, ["GAI_ID", "Type", "Bank_Width", "Stream_Nam", "GPS_Date"]) as cursor1:
                        for row1 in cursor1:
                            GAI_ID, Type, Bank_Width, Stream_Name, GPS_Date = row1[0], row1[1], row1[2], row1[3], row1[4]
                            with arcpy.da.UpdateCursor(stream_line, ["GAI_ID", "Stream_Type", "Bank_Width_Feet", "Stream_Nam", "GPS_Date"]) as cursor2:
                                for row2 in cursor2:
                                    for i in range(0,len(update_fields)):
                                        row2[i] = row1[i]
                                        cursor2.updateRow(row2)
                    edit.stopOperation()
                    edit.stopEditing(True)                
                    #arcpy.Append_management(stream_line, ENV_GDB + "\Streams", "NO_TEST")

                    #Garbage Collect
                    #arcpy.Delete_management(end_point)
                    #arcpy.Delete_management(start_point)

                #If line is single bank but fails coincidence test, draw in reverse order.
                elif downstream_center == False or upstream_center == False:
                    #Stream has been drawn from downstream to upstream. Switch order of flag num by multiplying by -1. Draw line in this order which will draw stream in appropriate direction.
                    arcpy.SelectLayerByAttribute_management(stream_lyr, "CLEAR_SELECTION")
                    arcpy.Delete_management(stream_line)
                    arcpy.AddField_management(stream_lyr, field_name="Flag_neg", field_is_nullable="NULLABLE", field_is_required="NON_REQUIRED")
                    arcpy.CalculateField_management(stream_lyr, field="Flag_neg", expression="!Flag_Num!*-1", expression_type="PYTHON_9.3")
                    stream_line_inverse = arcpy.PointsToLine_management(stream_lyr, workspace + "\stream_line_" + str(ID_replace_final) + "uID_" + str(unique_ID), Line_Field = "Bank_Side", Sort_Field = "Flag_neg", Close_Line = "NO_CLOSE")
                    if ID == 'SPA-NGP-007':
                        print("Inverse reached")
                    for att in stream_att_list:
                        arcpy.AddField_management(*(stream_line_inverse,)+att)
                    #Update values of stream_line with values from stream_lyr points.
                    #Start editing
                    edit = arcpy.da.Editor(workspace)
                    edit.startEditing(False, True)
                    edit.startOperation()
                    update_fields = ["GAI_ID", "Type", "Bank_Width", "Stream_Nam", "GPS_Date"]
                    with arcpy.da.SearchCursor(stream_lyr, ["GAI_ID", "Type", "Bank_Width", "Stream_Nam", "GPS_Date"]) as cursor1:
                        for row1 in cursor1:
                            GAI_ID, Type, Bank_Width, Stream_Name, GPS_Date = row1[0], row1[1], row1[2], row1[3], row1[4]
                            with arcpy.da.UpdateCursor(stream_line_inverse, ["GAI_ID", "Stream_Type", "Bank_Width_Feet", "Stream_Nam", "GPS_Date"]) as cursor2:
                                for row2 in cursor2:
                                    for i in range(0,len(update_fields)):
                                        row2[i] = row1[i]
                                        cursor2.updateRow(row2)
                    edit.stopOperation()
                    edit.stopEditing(True)             
                    #arcpy.Append_management(stream_line, ENV_GDB + "\Streams", "NO_TEST")

                    #Garbage Collect
                    #arcpy.Delete_management(end_point)
                    #arcpy.Delete_management(start_point)

            #If line is double bank and passes coincidence test, attribute and append into data base. If line is double bank but does not pass coincidence test, determine which side(s) are incorrect, and draw correct and incorrect sides
            #accordingly.
            elif end_pt_cnt != 1:
                if downstream_left == True and upstream_left == True and downstream_right == True and upstream_right == True:
                    #Both banks have been drawn properly. Draw and attribute as is.
                    #Add attribute fields to stream_line from STREAM points
                    for att in stream_att_list:
                        arcpy.AddField_management(*(stream_line,)+att)
                    #Update values of stream_line with values from stream_lyr points.
                    #Start editing.
                    edit = arcpy.da.Editor(workspace)
                    edit.startEditing(False, True)
                    edit.startOperation()
                    update_fields = ["GAI_ID", "Type", "Bank_Width", "Stream_Nam", "GPS_Date"]
                    with arcpy.da.SearchCursor(stream_lyr, ["GAI_ID", "Type", "Bank_Width", "Stream_Nam", "GPS_Date"]) as cursor1:
                        for row1 in cursor1:
                            GAI_ID, Type, Bank_Width, Stream_Name, GPS_Date = row1[0], row1[1], row1[2], row1[3], row1[4]
                            with arcpy.da.UpdateCursor(stream_line, ["GAI_ID", "Stream_Type", "Bank_Width_Feet", "Stream_Nam", "GPS_Date"]) as cursor2:
                                for row2 in cursor2:
                                    for i in range(0,len(update_fields)):
                                        row2[i] = row1[i]
                                        cursor2.updateRow(row2)
                    edit.stopOperation()
                    edit.stopEditing(True)                
                    #arcpy.Append_management(stream_line, ENV_GDB + "\Streams", "NO_TEST")

                    #Garbage Collect
                    #arcpy.Delete_management(end_point)
                    #arcpy.Delete_management(start_point)
                elif downstream_left == True and upstream_left == True:
                    if downstream_right == False or upstream_right == False:
                        print("left true right false")
                        #Right bank has been drawn from downstream to upstream. Select just the right bank from stream_lyr to delete it as the left bank is drawn correctly and should be left as is.
                        #Switch order of flag num by multiplying by -1. Draw line in this order which will draw stream in appropriate direction.
                        arcpy.SelectLayerByAttribute_management(stream_lyr, "CLEAR_SELECTION")
                        arcpy.MakeFeatureLayer_management(stream_line, "stream_line_right", where_clause="Bank_Side = 'Right'")
                        #Note: DeleteFeatures_management allows user to delete the selected feature, while Delete_management does not.
                        arcpy.DeleteFeatures_management("stream_line_right")
                        arcpy.AddField_management(stream_lyr_right, field_name="Flag_neg", field_is_nullable="NULLABLE", field_is_required="NON_REQUIRED")
                        arcpy.CalculateField_management(stream_lyr_right, field="Flag_neg", expression="!Flag_Num!*-1", expression_type="PYTHON_9.3")
                        stream_line_right_inverse = arcpy.PointsToLine_management(stream_lyr_right, workspace + "\stream_line_right" + str(ID_replace_final) + "uID_" + str(unique_ID), Line_Field = "Bank_Side", Sort_Field = "Flag_neg", Close_Line = "NO_CLOSE")
                        #Add attribute fields to stream_line and stream_line_right_inverse from STREAM points.
                        for att in stream_att_list:
                            arcpy.AddField_management(*(stream_line,)+att)
                        for att in stream_att_list:
                            arcpy.AddField_management(*(stream_line_right_inverse,)+att)
                        #Update values of stream_line and stream_line_right_inverse with values from stream_lyr points.
                        #Start editing.
                        for stream in att_stream:
                            edit = arcpy.da.Editor(workspace)
                            edit.startEditing(False, True)
                            edit.startOperation()
                            update_fields = ["GAI_ID", "Type", "Bank_Width", "Stream_Nam", "GPS_Date"]
                            with arcpy.da.SearchCursor(stream_lyr, ["GAI_ID", "Type", "Bank_Width", "Stream_Nam", "GPS_Date"]) as cursor1:
                                for row1 in cursor1:
                                    GAI_ID, Type, Bank_Width, Stream_Name, GPS_Date = row1[0], row1[1], row1[2], row1[3], row1[4]
                                    with arcpy.da.UpdateCursor(stream_line, ["GAI_ID", "Stream_Type", "Bank_Width_Feet", "Stream_Nam", "GPS_Date"]) as cursor2:
                                        for row2 in cursor2:
                                            for i in range(0,len(update_fields)):
                                                row2[i] = row1[i]
                                                cursor2.updateRow(row2)
                                    with arcpy.da.UpdateCursor(stream_line_right_inverse, ["GAI_ID", "Stream_Type", "Bank_Width_Feet", "Stream_Nam", "GPS_Date"]) as cursor3:
                                        for row3 in cursor3:
                                            for i in range(0,len(update_fields)):
                                                row3[i] = row1[i]
                                                cursor3.updateRow(row3)
                            edit.stopOperation()
                            edit.stopEditing(True)                
                        #arcpy.Append_management(stream_line, ENV_GDB + "\Streams", "NO_TEST")

                        #Garbage Collect
                        #arcpy.Delete_management(end_point)
                        #arcpy.Delete_management(start_point)
                elif downstream_right == True and upstream_right == True:
                    if downstream_left == False or upstream_left == False:
                        print("test")
                        #Left bank has been drawn from downstream to upstream. Select just the left bank from stream_lyr to delete it as the right bank is drawn correctly and should be left as is.
                        #Switch order of flag num by multiplying by -1. Draw line in this order which will draw stream in appropriate direction.
                        arcpy.SelectLayerByAttribute_management(stream_lyr, "CLEAR_SELECTION")
                        arcpy.MakeFeatureLayer_management(stream_line, "stream_line_left", where_clause="Bank_Side = 'Left'")
                        #Note: DeleteFeatures_management allows user to delete the selected feature, while Delete_management does not.
                        arcpy.DeleteFeatures_management("stream_line_left")
                        arcpy.AddField_management(stream_lyr_left, field_name="Flag_neg", field_is_nullable="NULLABLE", field_is_required="NON_REQUIRED")
                        arcpy.CalculateField_management(stream_lyr_left, field="Flag_neg", expression="!Flag_Num!*-1", expression_type="PYTHON_9.3")
                        stream_line_left_inverse = arcpy.PointsToLine_management(stream_lyr_left, workspace + "\stream_line_left" + str(ID_replace_final) + "uID_" + str(unique_ID), Line_Field = "Bank_Side", Sort_Field = "Flag_neg", Close_Line = "NO_CLOSE")
                        #Add attribute fields to stream_line and stream_line_left_inverse from STREAM points.
                        for att in stream_att_list:
                            arcpy.AddField_management(*(stream_line,)+att)
                        for att in stream_att_list:
                            arcpy.AddField_management(*(stream_line_left_inverse,)+att)
                        #Update values of stream_line and stream_line_left_inverse with values from stream_lyr points.
                        #Start editing.
                        for stream in att_stream:
                            edit = arcpy.da.Editor(workspace)
                            edit.startEditing(False, True)
                            edit.startOperation()
                            update_fields = ["GAI_ID", "Type", "Bank_Width", "Stream_Nam", "GPS_Date"]
                            with arcpy.da.SearchCursor(stream_lyr, ["GAI_ID", "Type", "Bank_Width", "Stream_Nam", "GPS_Date"]) as cursor1:
                                for row1 in cursor1:
                                    GAI_ID, Type, Bank_Width, Stream_Name, GPS_Date = row1[0], row1[1], row1[2], row1[3], row1[4]
                                    with arcpy.da.UpdateCursor(stream_line, ["GAI_ID", "Stream_Type", "Bank_Width_Feet", "Stream_Nam", "GPS_Date"]) as cursor2:
                                        for row2 in cursor2:
                                            for i in range(0,len(update_fields)):
                                                row2[i] = row1[i]
                                                cursor2.updateRow(row2)
                                    with arcpy.da.UpdateCursor(stream_line_left_inverse, ["GAI_ID", "Stream_Type", "Bank_Width_Feet", "Stream_Nam", "GPS_Date"]) as cursor3:
                                        for row3 in cursor3:
                                            for i in range(0,len(update_fields)):
                                                row3[i] = row1[i]
                                                cursor3.updateRow(row3)
                            edit.stopOperation()
                            edit.stopEditing(True)                
                        #arcpy.Append_management(stream_line, ENV_GDB + "\Streams", "NO_TEST")

                        #Garbage Collect
                        #arcpy.Delete_management(end_point)
                        #arcpy.Delete_management(start_point)
                else:
                    #Both banks have been drawn from downstream to upstream. Switch order of flag num by multiplying by -1. Draw line in this order which will draw streams in appropriate direction.
                    #Note: DeleteFeatures_management allows user to delete the selected feature, while Delete_management does not.
                    arcpy.DeleteFeatures_management(stream_line)
                    arcpy.AddField_management(stream_lyr, field_name="Flag_neg", field_is_nullable="NULLABLE", field_is_required="NON_REQUIRED")
                    arcpy.CalculateField_management(stream_lyr, field="Flag_neg", expression="!Flag_Num!*-1", expression_type="PYTHON_9.3")
                    stream_line_inverse = arcpy.PointsToLine_management(stream_lyr, workspace + "\stream_line_" + str(ID_replace_final) + "uID_" + str(unique_ID), Line_Field = "Bank_Side", Sort_Field = "Flag_neg", Close_Line = "NO_CLOSE")
                    #Add attribute fields to stream_line_inverse from STREAM points.
                    for att in stream_att_list:
                        arcpy.AddField_management(*(stream_line_inverse,)+att)
                    #Update values of stream_line_inverse with values from stream_lyr points.
                    #Start editing.
                    edit = arcpy.da.Editor(workspace)
                    edit.startEditing(False, True)
                    edit.startOperation()
                    update_fields = ["GAI_ID", "Type", "Bank_Width", "Stream_Nam", "GPS_Date"]
                    with arcpy.da.SearchCursor(stream_lyr, ["GAI_ID", "Type", "Bank_Width", "Stream_Nam", "GPS_Date"]) as cursor1:
                        for row1 in cursor1:
                            GAI_ID, Type, Bank_Width, Stream_Name, GPS_Date = row1[0], row1[1], row1[2], row1[3], row1[4]
                            with arcpy.da.UpdateCursor(stream_line_inverse, ["GAI_ID", "Stream_Type", "Bank_Width_Feet", "Stream_Nam", "GPS_Date"]) as cursor2:
                                for row2 in cursor2:
                                    for i in range(0,len(update_fields)):
                                        row2[i] = row1[i]
                                        cursor2.updateRow(row2)
                    edit.stopOperation()
                    edit.stopEditing(True)                
                    #arcpy.Append_management(stream_line, ENV_GDB + "\Streams", "NO_TEST")

                    #Garbage Collect
                    #arcpy.Delete_management(end_point)
                    #arcpy.Delete_management(start_point)
                    
        except:
            print("Unknown error. Adding " + str(ID) + " to Stream_IDs_Review.")
            Stream_IDs_REVIEW.append(ID)                    
                        
                        
                        
                    
                    
                

                  
                  
    
#print Stream_IDs_REVIEW to see if any flags have the same number.
#print("Streams to review: " + str(arcpy.GetCount_management(Stream_IDs_REVIEW).getOutput(0)))
print("Stream_IDs_REVIEW after: " + str(Stream_IDs_REVIEW))
#field_names = [f.name for f in arcpy.ListFields(STREAM)]
#print(field_names)
end_time = datetime.datetime.now()
elapsed_time = end_time-start_time
print("Elapsed time: " + str(elapsed_time))


#Wetlands
##########################################################################################################################################################################################################################################
##########################################################################################################################################################################################################################################
##########################################################################################################################################################################################################################################


