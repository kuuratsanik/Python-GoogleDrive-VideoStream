'''
    Copyright (C) 2014-2016 ddurdle

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.


'''
import anydbm

class scheduler:
    # Settings

    TYPE_STOPPED = 0
    TYPE_RUNNING = 1

    ##
    ##
    def __init__(self, settings=None, dbmfile=None):

        self.settings= settings
        #self.dbmfile = dbmfile
        #setup encryption password

        #self.dbm = anydbm.open(dbmfile,'c')


    # instanceName
    # frequency
    # lastRun
    # folder
    # type

    # type - 0 exhaustive, 1 changes only
    def setScheduleTask(self, instanceName, frequency, folder, type, cmd):
        count = self.countScheduledTask() + 1

        job=0
        while (job < count):
            #if self.dbm[str(job) + '_instance'] == str(instanceName) and self.dbm[str(job) + '_frequency'] == str(frequency) and self.dbm[str(job) + '_folder'] == str(folder) and self.dbm[str(job) + '_type'] == str(type):
            if self.settings.getSetting(str(job) + '_instance') == str(instanceName) and self.settings.getSetting(str(job) + '_frequency') == str(frequency) and self.settings.getSetting(str(job) + '_folder') == str(folder) and self.settings.getSetting(str(job) + '_type') == str(type):
                break
            job += 1
        #self.dbm[str(job) + '_instance'] = str(instanceName)
        #self.dbm[str(job) + '_frequency'] = str(frequency)
        #self.dbm[str(job) + '_folder'] = str(folder)
        #self.dbm[str(job) + '_type'] = str(type)
        #self.dbm[str(job) + '_runtime'] = str(0)
        #self.dbm[str(job) + '_stauts'] = str(self.TYPE_STOPPED)

        self.settings.setSetting(str(job) + '_instance', str(instanceName))
        self.settings.setSetting(str(job) + '_frequency', str(frequency))
        self.settings.setSetting(str(job) + '_folder', str(folder))
        self.settings.setSetting(str(job) + '_type', str(type))
        self.settings.setSetting(str(job) + '_runtime', str(0))
        self.settings.setSetting(str(job) + '_cmd', str(cmd))
        self.settings.setSetting(str(job) + '_statusDetail', '')
        self.settings.setSetting(str(job) + '_status', str(self.TYPE_STOPPED))

        print "updating job " + str(job) + "\n"
        #key = instanceName_type_frequency_folder
        return

    # type - 0 exhaustive, 1 changes only
    def recordScheduleTask(self, job,instanceName, frequency, folder, type, runtime, cmd, statusDetail, status):
        #key = instanceName_type_frequency_folder
        return

    def getScheduledTask(self, job):

        try:
            #return [self.dbm[str(job) + '_instance'], self.dbm[str(job) + '_frequency'], self.dbm[str(job) + '_folder'], self.dbm[str(job) + '_type'], self.dbm[str(job) + '_runtime'], self.dbm[str(job) + '_stauts']]
            return [self.settings.getSetting(str(job) + '_instance'), self.settings.getSetting(str(job) + '_frequency'), self.settings.getSetting(str(job) + '_folder'), self.settings.getSetting(str(job) + '_type'), self.settings.getSetting(str(job) + '_runtime'), self.settings.getSetting(str(job) + '_cmd'), self.settings.getSetting(str(job) + '_statusDetail'), self.settings.getSetting(str(job) + '_status')]
        except:
            return None

    def countScheduledTask(self):
        count = 0
        while (1):
            try:
                setting = self.settings.getSetting(str(count) + '_instance',None)
                if setting is None:
                    return count-1
                #self.dbm[str(count) + '_instance']
                count += 1
            except:
                return count-1

    def saveChangeNumber(self, instanceName, folderID,changeNumber):
        #self.dbm[instanceName + '_changenumber'] = changeNumber
        self.settings.setSetting(instanceName + '_'+str(folderID)+'_changenumber', changeNumber)

    def getChangeNumber(self, instanceName, folderID):
        #return self.dbm[instanceName + '_changenumber']
        self.settings.getSetting(instanceName + '_'+str(folderID)+'_changenumber')

